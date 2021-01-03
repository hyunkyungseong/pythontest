import os, sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
from slacker import Slacker
import time, calendar

slack = Slacker('xoxb-1597808694178-1598074312450-NBKedtTkjbflEnMIBuj3zfon')
def dbgout(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    slack.chat.post_message('#stock', strbuf)

def printlog(message, *args):
    """인자로 받은 문자열을 파이썬 셸에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message, *args)
 
# 크레온 플러스 공통 OBJECT
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpStock = win32com.client.Dispatch('DsCbo1.StockMst')
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311')  

def check_creon_system():
    """크레온 플러스 시스템 연결 상태를 점검한다."""
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        printlog('check_creon_system() : admin user -> FAILED')
        return False
 
    # 연결 여부 체크
    if (cpStatus.IsConnect == 0):
        printlog('check_creon_system() : connect to server -> FAILED')
        return False
 
    # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
    if (cpTradeUtil.TradeInit(0) != 0):
        printlog('check_creon_system() : init trade -> FAILED')
        return False
    return True

def get_current_price(code):
    """인자로 받은 종목의 현재가, 매수호가, 매도호가를 반환한다."""
    cpStock.SetInputValue(0, code)  # 종목코드에 대한 가격 정보
    cpStock.BlockRequest()
    item = {}
    item['cur_price'] = cpStock.GetHeaderValue(11)   # 현재가
    item['ask'] =  cpStock.GetHeaderValue(16)        # 매수호가
    item['bid'] =  cpStock.GetHeaderValue(17)        # 매도호가    
    return item['cur_price'], item['ask'], item['bid']

def get_ohlc(code, qty):
    """인자로 받은 종목의 OHLC 가격 정보를 qty 개수만큼 반환한다."""
    cpOhlc.SetInputValue(0, code)           # 종목코드
    cpOhlc.SetInputValue(1, ord('2'))        # 1:기간, 2:개수
    cpOhlc.SetInputValue(4, qty)             # 요청개수
    cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5]) # 0:날짜, 2~5:OHLC
    cpOhlc.SetInputValue(6, ord('D'))        # D:일단위
    cpOhlc.SetInputValue(9, ord('1'))        # 0:무수정주가, 1:수정주가
    cpOhlc.BlockRequest()
    count = cpOhlc.GetHeaderValue(3)   # 3:수신개수
    columns = ['open', 'high', 'low', 'close']
    index = []
    rows = []
    for i in range(count): 
        index.append(cpOhlc.GetDataValue(0, i)) 
        rows.append([cpOhlc.GetDataValue(1, i), cpOhlc.GetDataValue(2, i),
            cpOhlc.GetDataValue(3, i), cpOhlc.GetDataValue(4, i)]) 
    df = pd.DataFrame(rows, columns=columns, index=index) 
    return df

def get_target_price(code):
    """매수 목표가를 반환한다."""
    try:
        time_now = datetime.now()
        str_today = time_now.strftime('%Y%m%d')
        ohlc = get_ohlc(code, 10)
        if str_today == str(ohlc.iloc[0].name):
            today_open = ohlc.iloc[0].open 
            lastday = ohlc.iloc[1]
        else:
            lastday = ohlc.iloc[0]                                      
            today_open = lastday[3]
        lastday_high = lastday[1]
        lastday_low = lastday[2]
        target_price = today_open + (lastday_high - lastday_low) * 0.5
        return target_price
    except Exception as ex:
        dbgout("`get_target_price() -> exception! " + str(ex) + "`")
        return None

def get_movingaverage(code, window):
    """인자로 받은 종목에 대한 이동평균가격을 반환한다."""
    try:
        time_now = datetime.now()
        str_today = time_now.strftime('%Y%m%d')
        ohlc = get_ohlc(code, 20)

        print(ohlc)

        if str_today == str(ohlc.iloc[0].name):
            lastday = ohlc.iloc[1].name
        else:
            lastday = ohlc.iloc[0].name
        closes = ohlc['close'].sort_index()         
        ma = closes.rolling(window=window).mean()
        return ma.loc[lastday]
    except Exception as ex:
        dbgout('get_movingavrg(' + str(window) + ') -> exception! ' + str(ex))
        return None    

if __name__ == '__main__': 

    code = 'A005250'

    objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
    objStockMst.SetInputValue(0, code)   #종목 코드 - 삼성전자
    objStockMst.BlockRequest()
    
    # 현재가 통신 및 통신 에러 처리 
    rqStatus = objStockMst.GetDibStatus()
    rqRet = objStockMst.GetDibMsg1()
    print("통신상태", rqStatus, rqRet)
    if rqStatus != 0:
        exit()
    
    # 현재가 정보 조회
    name= objStockMst.GetHeaderValue(1)  # 종목명


    print(name)    
    print(get_ohlc(code, 20))
  


    # try:
    #     symbol_list = ['A122630', 'A252670', 'A233740', 'A250780', 'A225130',
    #          'A280940', 'A261220', 'A217770', 'A295000', 'A176950']
    #     symbol_list = ['A005250']

    #     bought_list = []     # 매수 완료된 종목 리스트
    #     target_buy_count = 5 # 매수할 종목 수
    #     buy_percent = 0.19   
    #     printlog('check_creon_system() :', check_creon_system())  # 크레온 접속 점검
    #     stocks = get_stock_balance('ALL')      # 보유한 모든 종목 조회
    #     total_cash = int(get_current_cash())   # 100% 증거금 주문 가능 금액 조회
    #     buy_amount = total_cash * buy_percent  # 종목별 주문 금액 계산
    #     printlog('100% 증거금 주문 가능 금액 :', total_cash)
    #     printlog('종목별 주문 비율 :', buy_percent)
    #     printlog('종목별 주문 금액 :', buy_amount)
    #     printlog('시작 시간 :', datetime.now().strftime('%m/%d %H:%M:%S'))
    #     soldout = False


    #     while True:
    #         t_now = datetime.now()
    #         t_9 = t_now.replace(hour=9, minute=0, second=0, microsecond=0)
    #         t_start = t_now.replace(hour=9, minute=5, second=0, microsecond=0)
    #         t_sell = t_now.replace(hour=15, minute=15, second=0, microsecond=0)
    #         t_exit = t_now.replace(hour=15, minute=20, second=0,microsecond=0)
    #         today = datetime.today().weekday()
    #         if today == 5 or today == 6:  # 토요일이나 일요일이면 자동 종료
    #             printlog('Today is', 'Saturday.' if today == 5 else 'Sunday.')
    #             sys.exit(0)
    #         if t_9 < t_now < t_start and soldout == False:
    #             soldout = True
    #             sell_all()
    #         if t_start < t_now < t_sell :  # AM 09:05 ~ PM 03:15 : 매수
    #             for sym in symbol_list:
    #                 if len(bought_list) < target_buy_count:
    #                     buy_etf(sym)
    #                     time.sleep(1)
    #             if t_now.minute == 30 and 0 <= t_now.second <= 5: 
    #                 get_stock_balance('ALL')
    #                 time.sleep(5)
    #         if t_sell < t_now < t_exit:  # PM 03:15 ~ PM 03:20 : 일괄 매도
    #             if sell_all() == True:
    #                 dbgout('`sell_all() returned True -> self-destructed!`')
    #                 sys.exit(0)
    #         if t_exit < t_now:  # PM 03:20 ~ :프로그램 종료
    #             dbgout('`self-destructed!`')
    #             sys.exit(0)
    #         time.sleep(3)
    # except Exception as ex:
    #     dbgout('`main -> exception! ' + str(ex) + '`')