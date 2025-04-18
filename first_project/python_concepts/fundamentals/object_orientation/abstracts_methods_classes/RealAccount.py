from first_project.python_concepts.fundamentals.object_orientation.abstracts_methods_classes.CustomerAccount import \
    CustomerAccount

class RealAccount(CustomerAccount):
    def __init__(self, number, iof, ir, amount_invested, yield_rate):
        self.number = number
        self.iof = iof
        self.ir = ir
        self.amount_invested = amount_invested
        self.yield_rate = yield_rate

    def performance_calculation(self):
        pass

c_1 = RealAccount(1233, 0.8, 0.7, 1000, 500)
print(f"Account number: {c_1.number}")
print(f'Amount invested: {c_1.amount_invested}')

