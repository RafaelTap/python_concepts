class Account_2:
    def __init__(self, number, balance):
        self._number = number  #accessed only internally
        self._balance = balance  #accessed only internally

    @property  #decorated method (getter)
    def balance(self):
        return self._balance

    @balance.setter #privates attributes to pass through this method (setter)
    def balance(self, balance):
        if balance < 0:
            print("invalid balance")
        else:
            self._balance = balance

def main():
    ac_2 = Account_2(2233,0)
    ac_2.balance = 10 #@setter
    print(f'Balance: {ac_2.balance}')#@property(getter)

if __name__ == "__main__":
    main()