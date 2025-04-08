class MyClass:
    def __init__(self):
        self._private_name = "Rafael Taparica"
        self._private_age = 35

    def _private_method(self): #private with one underscore
        print("private method")

    def __private_show_info(self): #private with two underscore(strongly private)
        print(f'{self._private_name}\n{self._private_age}')

    def personal_info(self): #method that can access privates methods. It's a public method
        self.__private_show_info()

    #static method
    @staticmethod
    def static_method(x,y):
        return x + y