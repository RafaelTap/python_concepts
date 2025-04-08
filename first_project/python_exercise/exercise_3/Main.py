from first_project.python_exercise.exercise_3.Cow import Cow
from first_project.python_exercise.exercise_3.Dog import Dog
from first_project.python_exercise.exercise_3.Duck import Duck

dog = Dog("ramires")
cow = Cow("mimosa")
duck = Duck("donald")

print(dog.move())
print(dog.speak())
print(" ")
print(cow.speak())
print(cow.move())
print(" ")
print(duck.move())
print(duck.speak())
print(duck.flying())
print(duck.swimming())
