# python oriented to object

# communication between objects

#creating method to communicate two differents objects

class Account:
    def __init__(self, accountNumber, docNumber, name, balance):
        self.accountNumber = accountNumber
        self.docNumber = docNumber
        self.name = name
        self.balance = balance

    def deposit(self, value):
       self.balance += value

    def withdraw(self, value):
       if self.balance < value: #check if the account has balance
           return False
       else:
           self.balance -= value
           return True

    def bank_statement(self):
       print(f'Name: {self.name}\nAccount: {self.accountNumber}\nBalance: $ {self.balance}')

    def bank_transfer(self, destination_account, value):
        if self.balance < value:
            print("Insufficient balance")
        else:
            destination_account.deposit(value)
            self.balance -= value
            print("transfer made")
            self.bank_statement()

def main():
    account_1 = Account(2233, "13465467879", "Rafael Taparica", 13576.78)
    account_2 = Account(3322, "57694837657", "Gabriela Bastos", 14000)

    account_1.bank_transfer(account_2, 545.67)

if __name__ == "__main__":
    main()