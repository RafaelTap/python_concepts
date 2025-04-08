
class Bank:
    def  __init__(self, name, bank_code):
        self.name = name
        self.bank_code = bank_code
        self.accounts = []

    def add_account(self, customer_account):
        self.accounts.append(customer_account)

    #this method is polymorph, calculate the month rental
    def month_performance(self):
        for a in self.accounts:
            a.peformance_calculation()


    def print_balance(self):
        for a in self.accounts:
            a.extract()