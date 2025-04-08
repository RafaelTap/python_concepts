from first_project.python_exercise.exercise_3.Animal import Animal
from first_project.python_exercise.exercise_3.Flying import Flying
from first_project.python_exercise.exercise_3.Swimmer import Swimmer


class Duck(Animal, Flying, Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "qua  qua"

    def move(self):
        return f'{self.name} moves with two paws'

    def swimming(self):
        return f"{self.name} is swimming"

    def flying(self):
        return f"{self.name} is flying"