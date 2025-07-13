class CustomizedException(Exception):
    pass

    def check_value(value):
        if value < 0:
            raise CustomizedException("value can't be negative")

    # method that throw exception if called
    def division(a, b):
        return a + b
