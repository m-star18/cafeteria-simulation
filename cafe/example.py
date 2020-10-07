class Toyota:
    def __init__(self):
        self.TABLE = 50
        self.NUMBER = 6
        self.SUM_NUMBER = [self.NUMBER] * self.TABLE
        self.SEATS = [[-1] * self.NUMBER for _ in range(self.TABLE)]
        self.data = [self.TABLE, self.SUM_NUMBER, self.SEATS]
