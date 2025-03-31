#Decision and repetition in python

# repetition estruct

# for with reserved word 'pass'

"""

the instruction 'pass' is a reserved space that do nothing.
when python finds the instruction 'pass', it continues the
program execution without do nothing.
the instruction 'pass' is used as a reserved space when the
syntax requires instructions, but you still don't implemented
the corresponded logic.

"""

for number in range(1,15):
    if number % 2 == 0:
        pass
    else:
        print(number)



