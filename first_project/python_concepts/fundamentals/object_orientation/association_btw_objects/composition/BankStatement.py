#this class is associated to Account class
class BankStatement:
    def __init__(self):
        self.transactions = [] #empty transaction list


    def extract(self, account_number):
        print(f'Extract: {account_number}\n')
        for transaction in self.transactions:
            print(f'{transaction[0]}: 15s {transaction[1]: 10.2f} {transaction[2]}'
                  f'{transaction[3].strftime("%d/%m/%y")}')