# precedence relationship between operators

"""

1 - [expressions ...]	list
2 - x[ ], x[index : index]	index operator
3 - **	Exponenciation
4 - +x, -x	positive and negative sign
5 - *, /, //, %	Product, division, whole division, rest
6 - +, -	Sum, subtraction
7 - in, not in, <, <=,>, >=, <>, !=, ==	Comparing, inclusive the occurrence in lists
8 - not x	Booleano NOT
9 - and	Booleano AND
10 - or	Booleano OR

"""

# data type conversions

"""
sometimes we need to convert types of variables, int to float, float to int, int to string
among others convertions 
 
"""

# numeric (int/float) to string
age = 19
height = 1.76
print("age-> ", age, "\nheight-> ", height)
print(type(age), type(height))

age_str = str(age) #age converted to string
height_str = str(height) #height converted to string
print("age-> ", age_str, "\nheight-> ", height_str)
print("Age_str type-> ", type(age_str), "\nheight_str type-> ", type(height_str))

#string to numeric (int/float)
grade1_str = "8.5"
grade2_str = "7"
print("biology grade 1: ", grade1_str, "\nbiology grade 2: ", grade2_str)
print("grade_str1 type -> ", type(grade1_str), "grade_str2 type ->", type(grade2_str))

grade1 = float(grade1_str)
grade2 = int(grade2_str)
print("biology grade 1: ", grade1, "\nbiology grade 2: ", grade2)
print("grade1 type -> ", type(grade1), "grade2 type ->", type(grade2))

#convertion between float and int

a = 3
b = 4.2
c = float(a)
d = int(b) # in this case, lost the decimal place

print("a = ", a, "b = ", b, "c = ", c, "d = ", d)

#boolean convertion in whole number ( 1 = true, 0 = false)

x = True + 4
y = False - 1

print("x = ", x, "y = ", y)