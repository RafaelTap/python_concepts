#DATA TYPE IN PYTHON

"""
Numeric type: include int, float (floating dot) and complex numbers,
to make mathematics operations and represents numerics values of any types.
sequential type: represents string (str), lists(list), tuples(tuple).
Dictionary type: mappings (dict)
boolean type: true or false
bool type: compare two numbers in math expression and return True or False.
"""

whole = 3 # int
floating = 3.0 # float
#type complex


r = complex (2,5)
print(type(r))
r.conjugate()

w = 2 + 5j
print(type(w))
w.conjugate()

#numeric operations
sum_ = 1 + 2 #sum
sub_ = 3 - 4 #subtraction
mult_ = 4 * 7 #multiplication
div_ = 10 / 2 #division
expo_ = 3 ** 2 #exponential
quoc_ = 21 // 2 #quocient (whole division)
mod_ = 21 % 2 #module (rest)
abs_ = abs(-4.73) #absolut value

print("sum result is: ", sum_)
print("subtraction result is: ", sub_)
print("multiplication result is: ", mult_)
print("division result is: ", div_)
print("square root is: ", expo_)
print("quotient is: ", quoc_)
print("module (rest) is: ", mod_)
print("Absolute value: ", abs_)

""" 

if you make a numeric operation with whole number and a number with floating dot,
the result will be a floating dot number.

"""
result = whole + floating
print("result is: ",result)
#boolean
bln_f = False
bln_t = True

# for more math functions we can use the modules math and fraction.



