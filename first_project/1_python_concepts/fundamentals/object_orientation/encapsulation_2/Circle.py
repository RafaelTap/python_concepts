class Circle:
    __circleTotal = 0 #class attribute out of __init__ method

    def __init__(self, x, y, r):
        self._x = x
        self._y = y
        self._r = r
        type(self).__circleTotal += 1 #each time an object is made, will sum one(1) to total of objects(circles).
        #it allows that the code works correctly been used in subclasses.

    @classmethod
    def get_total_circle(cls): #the first parameters usually is "cls".
        return cls.__circleTotal

