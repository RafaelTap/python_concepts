from datetime import datetime
# string formatting
# three ways to formatting strings
#f-string, format() and manually

""" f-string"""
name = "rafael"
my_string = f"i'm  {35} years old"
my_string_2 = f"name: {name.upper()}"
my_string_3 = f"result: {2 > 1}"
my_string_4 = f"two is in the list: {2 in [3,4,6,8]}"
my_string_5 = f"sum: {3 + 4}"
print(my_string)
print(my_string_2)
print(my_string_3)
print(my_string_4)
print(my_string_5)

#time, float and width
print("\ntime, float and width\n")

fruits = ["banana", "grape", "strawberry", "lemon", "blueberry"]
for fruit in fruits:
    my_fruits = f"name: {fruit:12} - number of letters: {len(fruit): 3}"
    print(my_fruits)

print()

pi = 3.1415
my_pi = f"pi = {pi:.1f}"
pi_outOfPlace = f"pi = {pi:6.2f}"
my_real_pi = f"pi = {pi:.4f}"

print(my_pi)
print(pi_outOfPlace)
print(my_real_pi)

print()

date = datetime.now()
my_date = f"today is: {date}"
my_date_2 = f"formatted date: {date:%d/%m/%y}"

print(my_date)
print(my_date_2)







