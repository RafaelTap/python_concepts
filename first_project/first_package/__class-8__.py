# there are three scopes
"""
Global scope: all variable declared out a function;
Local scope: all variable declared within a function;
Function scope:

"""
def average():
    first_note = 7 #local variable
    second_note = 8 #local variable
    print((first_note + second_note) / 2)

text = "Average is: " # global variable

print(text)
average()
