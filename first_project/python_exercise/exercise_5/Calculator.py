class Calculator:

    def sum(self, a, b):
        try:
            return a + b
        except TypeError as e:
            print(e)

    def subtraction(self, a, b):
        try:
            return a - b
        except TypeError as e:
            print(e)

    def division(self, a, b):
        try:
            return a / b
        except TypeError as e:
            print(e)

    def multiplication(self, a, b):
        try:
            return a * b
        except TypeError:
            print("type error")


