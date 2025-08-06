# object oriented programming
class Factorial:
    def calculate (self,n):
        if n == 0:
            return 1
        else:
            return n * self.calculate(n-1)
        # it is an object of the class, instanced.
        f = Factorial ()
        print("result of factorial", f.calculate(8))

        """ many lines commented  """
    