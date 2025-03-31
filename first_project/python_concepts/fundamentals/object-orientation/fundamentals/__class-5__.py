# python oriented to object

#method with return, return a value, validate the object state

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
       print(f'Name: {self.name}\nAccount: {self.accountNumber}\nBalance: {self.balance}')

def main():
    account = Account(2233, "13465467879", "Rafael Taparica", 13456.76)
    withdraw_value = 500
    withdraw_result = account.withdraw(withdraw_value)
    if withdraw_result:
        print(f'Withdraw: {withdraw_value}\ncurrent balance: $ {account.balance}')
    else:
        print("Insufficient balance.")

if __name__ == "__main__":
    main()