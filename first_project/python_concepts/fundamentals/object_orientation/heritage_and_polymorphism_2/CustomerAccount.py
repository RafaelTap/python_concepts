class CustomerAccount:
    def __init__(self, number, iof, ir, amount_invested, yield_rate ):
        self.number = number
        self.iof = iof
        self.ir = ir
        self.amount_invested = amount_invested
        self.yield_rate = yield_rate

    def performance_calculation(self):
        remuneration = self.amount_invested * self.yield_rate
        iof_value = self.iof * remuneration
        ir_value = self.ir * remuneration
        self.amount_invested += remuneration - iof_value - ir_value

    def extract(self):
        print(f'Account: {self.number}\nBalance: {self.amount_invested}' )

