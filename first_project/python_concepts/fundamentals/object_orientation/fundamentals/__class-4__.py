# python oriented to object

# definition of the actions that the object can do

class Account:
    def __init__(self, accountNumber, docNumber, name, balance):
        self.accountNumber = accountNumber
        self.docNumber = docNumber
        self.name = name
        self.balance = balance

    def deposit(self, value):
       self.balance += value

    def withdraw(self, value):
       self.balance -= value

    def bank_statement(self):
       print(f'Name: {self.name}\nAccount: {self.accountNumber}\nBalance: $ {self.balance}')

def main():
   account = Account(2233, "13465467879", "Rafael Taparica", 12674.66)
   account.bank_statement()
   account.deposit(500)
   account.bank_statement()
   account.withdraw(1000)
   account.bank_statement()



if __name__ =="__main__":
    main()

