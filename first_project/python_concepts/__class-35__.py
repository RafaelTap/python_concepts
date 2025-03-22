#data types in python

#sequences and dictionary

#tuple: is the closest of the conception of register in python

"""
tuple: accept different data types;
string: accept only datas of the same type.
"""

htg_tuple = (1, "rafael", 3.6, [2,3,4], {"name":"rafael"})

#accessing elements from tuple

print(f'Whole: {htg_tuple[0]}\n')
print(f'String: {htg_tuple[1]}\n')
print(f'Float: {htg_tuple[2]}\n')
print(f'List: {htg_tuple[3]}\n')
print(f'Dictionary: {htg_tuple[4]}\n')

#modifying the list from tuple
htg_tuple[3].append(5)
print(htg_tuple, "\n")

#accessing a value in dictionary from tuple

value = htg_tuple[4]["name"]
print(value)

#iterating in tuple

for element in htg_tuple:
    print(f'Element: {element} Tipo: {type(element)}')


