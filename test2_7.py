class NasdaqStock:
    """
    Class for NASDAQ stocks
    """
    count = 0
    def __init__(self,symbol,price):
        """
        생성자
        """
        self.symbol = symbol
        self.price = price
        NasdaqStock.count += 1
        print('생성자 __init__({},{:.2f}) > count : {}'.format(self.symbol,self.price,NasdaqStock.count))

    def __del__(self):
        """
        소멸자
        """
        print('Calling __del__({})'.format(self))

gg=NasdaqStock('GOOG',1154.05)
del(gg)

ms=NasdaqStock('MSFT',102.44)
del(ms)

amz = NasdaqStock('AMZN',1746.00)
del(amz)

print(help(NasdaqStock))