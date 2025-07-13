# python oriented to object

#creating classes and instantiating objects

#creating classes

class Account:
    def __init__(self, accountNumber, docNumber, name, balance):
        self.accountNumber = accountNumber
        self.docNumber = docNumber
        self.name = name
        self.balance = balance

#instatiating objects

def main():
    a_1 = Account(2, 43576, "rafael", 1000.44)
    print(f'Account number: {a_1.accountNumber}')
    print(f'Name: {a_1.name}')
    print(f'Document:  {a_1.docNumber}')
    print(f'Balance: {a_1.balance}')

#running main method

if __name__ == "__main__":
    main()