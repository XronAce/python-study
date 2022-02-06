class Stock():
    def __init__(self, name, code, PER, PBR, divyield):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.divyield = divyield

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

    def set_per(self, PER):
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR
    
    def set_dividend(self, divyield):
        self.divyield = divyield

stocks = []

삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stocks.append(삼성전자)
stocks.append(현대차)
stocks.append(LG전자)

for stock in stocks:
    print(f"종목코드: {stock.code}, PER: {stock.PER}")