class Character:
    c = ''
    version = ''
    code1 = ''
    code2 = ''
    code3 = ''
    code4 = ''

    def __init__(self, d):
        self.__dict__ = d

    def get_code1(self):
        return self.code1

    def get_code2(self):
        return self.code2

    def get_code3(self):
        return self.code3

    def get_code4(self):
        return self.code4