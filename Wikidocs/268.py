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

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

print(삼성.divyield)