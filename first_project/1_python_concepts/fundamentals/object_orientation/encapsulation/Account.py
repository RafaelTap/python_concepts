class Account:
    def __init__(self, balance, account_number):
        self.__balance = balance #two underlines before word, indicate that the attribute is private
        self.__account_number = account_number ##two underlines before word, indicate that the attribute is private

    def show_balance(self):
        print(f'Account: {self.__account_number}\nBalance: {self.__balance}')


def main():
    ac_1 = Account(2300, 2233)
    #ac_1.balance # (AttributeError: 'Account' object has no attribute 'balance')
    balance_1 = ac_1._Account__balance #a way to transgressing the private access to attribute
    print(balance_1)
    ac_1.show_balance()

if __name__=="__main__":
    main()