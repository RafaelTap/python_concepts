class CustomizedError(Exception):
    def __init__(self,message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f'[Error: {self.error_code}]: {self.args[0]} '

    def function_throws_exception(value):
        if value < 0:
            raise CustomizedError("value can't be negative")
        else:
            return f'value is: {value}'

    try:
        result = function_throws_exception()
        print(result)
    except CustomizedError as e:
        print(e)