# # p71~72
# rsi = 88
# if rsi>70:
#     print('과매수 상태입니다')
# elif rsi < 30:
#     print('과매도 상태입니다')
# else:
#     print('정상입니다')
#  

# for i in [1,3,5]:
#     print(i)

# for i in range(7):
#     print(i)

# faang = ['FB','AMZN','AAPL','NFLX','GOOGL']
# for i,symbol     in enumerate(faang,0):
#     print(i,symbol)

# i=0
# while i>=0:
#     i+=1
#     if(i%2)==0:
#         continue
#     if i>5:
#         break
#     print(i)
# else:       
#     print('조건이 거짓')

# for i in [1,3,5]:
#     print(i)
# else:
#     print('for 문 종료 입니다')

# try:
#     1/0
# except Exception as e:
#     print('예외발생 : ' + str(e) )

# L = [[1,2],[3,4]]
# print(L[0][0])
# print(L[0][1])
# print(L[-1][0])
# print(L[-1][-1])

# print(L+L)
#print(L*3)

#mylist = 'one two three'.split()

# print(type(mylist))
# print(mylist)

#print(' '.join(mylist))


# p78
#sort() : list 에서만 사용가능 / 리스트를 직접 정렬함
#sorted() : list , 문자열,튜플,딕션너리 등 반복 가능한 자료형에 모두 사용됨
#           기존 리스트를 복사해서 새로 만듬

#li = [2,5,3,1,4]
#li.sort()
#print(li)

#print(li)
#print(sorted(li))

#append() : 인수의 자료형에 상관없이 리스트 뒤에 그대로 추가한다.  [1, 2, [3, 4]]
#extend() : 인수가 반복 자료형일 경우 반복 자료형 내부의 각 원소를 추가한다.  [1, 2, 3, 4]

#l = [1,2]
# l.append([3,4])
# print(l)

#l.extend([3,4])
#print(l)

# 구분자 변경하기
#nDate = '2020/12/27'
#mylist = nDate.split('/')
#print('-'.join(mylist))
#print('-'.join('2020/12/27'.split('/')))

#print('2020/12/27'.replace('/','-'))

# 천단위 숫자를 쉽표로
#print(format(123456,','))

# 리스트 복사
# 리스트는 인덱싱 , 슬라이싱 , 내장함수를 사용할 수 있다
# [:]를 사용하여 리스트를 복사할 수 있다.  [:]  :  전체 영역을 의미함

# mylist = ['one', 'two' , 'three']
# newlist = mylist[:]
# print(newlist)

## 리스트 내포 : 열거형 객체의 전체 또는 일부 원소를 변경하여 새로운 열거형 객체를 생성할 수 있다.
##              보통 다른 언어에서는  for 반복문으로 처리함.

# nums = [1,2,3,4,5]
# squares = []
# for x in nums:
#     squares.append(x**2)
# print(squares)

# nums = [1,2,3,4,5]
# squares = [x**2 for x in nums]
# print(squares)

# nums = [1,2,3,4,5]
# squares = [x**2 for x in nums if x % 2 == 0]
# print(squares)

## 변경이 불가능한 튜플 : 리스트 처럼 다양한 자료형의 원소를 가지지만 대괄호 대신 소괄호로 표시하며
##                       원소를 변경할 수 없다(???).
## 튜플은 다른리스트나 내장함수도 원소로 가질 수 있음

# myTuple = ['a','b','c',[10,20,30],abs,max]

# print(myTuple[3])
# print(myTuple[4](-100))
# print(myTuple[5](myTuple[3]))
# myTuple[0] = 'd'
# print(myTuple)

## {키:값} 형태 딕셔너리
## 순서가 없는 집합
## 키:값 형태의 원소들을 쉼표로 구분하여 중괄호로 감싸서 표시한다
## 인덱스로 값에 접근하는 것은 불가능하다.(KeyError)

# crispr = {'EDIT':'Editas Medicine','NTLA':'Intellia Theraeutics'}
# #print(crispr[0])    # KeyError: 0

# print(crispr['NTLA'])

# crispr['CRSP'] = 'CRISPR Therapeutics'

# print(crispr)

## 문자열 포맷 출력     p83 ~ p85
## % 기호 , {} , f-strings  방식이 있다
## %s : 문자열  , %c : 문자 ,  %d : 십진수  , %f : 부동소수 , %x : 16진수

# crispr = {'EDIT':'Editas Medicine','NTLA':'Intellia Theraeutics'}

# for x in crispr:
    
#     print('%s : %s'  % (x , crispr[x]))         # print('%s : %s' , % (x , crispr[x]))   오류  '%s : %s' ,
#     print('{} : {}'.format(x,crispr[x]))
#     print(f'{x} : {crispr[x]}')                 

## 중복없는 셋 중괄호 , 생성한 순서대로 원소가 저장되지 않음

# s ={'A','P','P','L','E'}
# print(s)

# ## 셋 내부에 특정원소가 존재하는지 검사하려면 if ~ in
# if 'P' in s:
#     print('\'P\' 는 SET {}에 존재한다 '.format(s) )

## set은 인덱싱이 불가능한 대신, 원소들의 교집합,합집합,차집합을 구할 수 있다.
# setA = {1,2,3,4,5}
# setB = {3,4,5,6,7}

# print(setA & setB)
# print(setA | setB)
# print(setA - setB)
# print(setB - setA)

## 셋은 반복 자료형처럼 리터럴로 원소가 없는 상태에서 생성할 수 없다
# ls = []         # list
# d = {}          # dic
# t = ()          # tupple
# s = set()       # set

# ls = [1,3,5,2,2,3,4,2,1,1,1,5]
# print(list(ls))
# print(list(set(ls)))

## timeit 으로 성능 측정하기
## timeit(테스트 구문 , setup=테스트준비구문 , number = 테스트반복횟수)
#import timeit

# iteration_test = '''
# for i in itr :
#     pass
# '''
# print(timeit.timeit(iteration_test,setup='itr = list(range(10000))',number=1000))
# print(timeit.timeit(iteration_test,setup='itr = tuple(range(10000))',number=1000))
# print(timeit.timeit(iteration_test,setup='itr = set(range(10000))',number=1000))

# iteration_test = ''' 
# import random
# x= random.randint(0,len(itr)-1)
# if x in itr:
#      pass
# '''

# print(timeit.timeit(iteration_test,setup='itr = list(range(10000))',number=1000))
# print(timeit.timeit(iteration_test,setup='itr = tuple(range(10000))',number=1000))
# print(timeit.timeit(iteration_test,setup='itr = set(range(10000))',number=1000))

## dir()함수
# s='string'
# print(type(s))
# print(dir())

# print(help('keywords'))

## 함수
## 연평균성장율(CAGR) = 복합연평균성장률 = 연복리 수익률
## 1년 동안 얼마 만큼씩 증가하는지를 나타내는 값으로, 주로 투자수익률을
## 표시하는데 사용되지만,판매수량이나 사용자 증가율 등을 나타낼 때도 쓴다.
## CAGR = (L/F)**(1/Y)-1    F : 처음값    L : 마지막값    Y : 처음값과 마지막 값 사이의 연(YEAR) 수
## 클래스에 속하지 않는 경우 함수 , 클래스에 속하는 경우 메소드

# def getCAGR(first , last , years):
#     return ((last/first)**(1/years) - 1) * 100


# print('연평균 수익률은 {:.2f}% 입니다.'.format(getCAGR(65300,2669000,20)))

# print(type(None))

# def func1():
#     pass

# print(func1()==None)

## 여러 결괏값 반환
## 튜플 객체로 변환되어 반환된다.
## 반환한 순서대로 여러 객체로 나누어 받으려면 변수를 쉼표로 구분하여 받으면 됨
# def myFunc():
#     var1 = 'a'
#     var2 = [1,2,3]
#     var3 = max
#     return var1 , var2 , var3
# print(myFunc())

# s,l,f = myFunc()
# print('{},{},{}'.format(s,l,f))

## 람다 : 이름없는 간단한 함수를 만들 때 사용한다.
# insertComma = lambda x:  format(x,',')
# print(insertComma(1234567))

## 모듈과 패키지        p97
## .py확장자를 갖는 파일 모두를 모듈이라 부를 수 있다
## 여러모듈(.py)을 특정 디렉토리에 모아놓은 것을 패키지라 부르며
## 이러한 모듈 또는 패키지를 가리켜 라이브러리 라고 부른다.
## 표준라이브러리 / 외부라이브러리
## 표준라이브러리는 별도의 설치없이 import 명령으로 바로 불러와서 사용함.
## 외부라이브러리는 사용자가 직접 설치 후 import 명령으로 불러와서 사용함.

# print(help('datetime'))

## 모듈의 위치를 알 수 있는 속성   .__file__
# import datetime
# print(datetime.__file__)

## from ~ import ~ 
## from 모듈명 import 클래스명 , 함수 명
## from 패키지명 import 모듈명
## import ~ as ~  : 이름이 긴 모듈명을 프로그래머가 원하는 별칭으로 줄여서 사용

# import calendar             ## 모듈명을 먼저 적어주어야 한다  'calendar.'
# print(calendar.month(2020,12))

# from calendar import month  ## 모듈명 없이 메소드명을 바로 사용 할 수 있다.
# print(month(2020,12))

# import datetime
# print(datetime.datetime.now())

# from datetime import datetime as dt
# print(dt.now())


# import urllib.request
# print(type(urllib.request))

## 패키지의 경로 속성 : 경로 속성을 갖는 것들만 패키지다
# import urllib
# print(type(urllib))
# print(urllib.__package__)

## __name__  :  변수이름이 아니라  정의 시 정의된 이름
import  myPackage.moduleA


