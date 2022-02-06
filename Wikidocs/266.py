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
