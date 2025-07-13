from Circle import Circle
from MyClass import MyClass

c1 = Circle(1,2,20)
print(c1.get_total_circle())

c2 = Circle(2,2,20)
print(c2.get_total_circle())

c3 = Circle(3,3,30)
print(c3.get_total_circle())

me = MyClass()
me.personal_info()

print("transgressing the private method")
me._MyClass__private_show_info()

print("Using static method with a object")
print(f'{me.static_method(2,5)}')

print("Using static method directly from the class, is not necessary create a instance of class")
result = MyClass.static_method(4,4)
print(result)