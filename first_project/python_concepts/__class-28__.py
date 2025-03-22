#Decision and repetition in python

# repetition estruct

# for with reserved word 'continue'

"""

the instruction 'continue' is used inside a loop (for and while)
to skip the actual iteration and go to the next.
When python interpreter finds the instruction 'continue', it
interrupts the actual iteration and skip to begin of the next
iteration.
it's used when you want skip some iterations inside a loop, based
on a specific condition.

"""
for number in range(1,11):
    if number == 5:
        continue # used to skip the number five(5).
    else:
        print(number)