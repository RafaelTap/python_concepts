# procedural programming
# reduced function, because reference itself.
def fatorial (n):
    if n == 0:
        return 1
    else:
        return n * fatorial (n-1)
    print("factorial result: ", fatorial(5))


