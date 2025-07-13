from first_project.python_concepts.fundamentals.object_orientation.heritage_and_polymorphism_2.CustomerAccount import \
    CustomerAccount

class PaidAccount(CustomerAccount):
    def __init__(self, number, iof, ir, amount_invested, yield_rate):
        super().__init__(number, iof, ir, amount_invested, yield_rate)

    def performance_calculation(self):
        remuneration = self.amount_invested * self.yield_rate
        self.amount_invested += remuneration

