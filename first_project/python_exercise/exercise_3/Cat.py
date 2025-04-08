from first_project.python_exercise.exercise_3.Animal import Animal

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "miau"

    def move(self):
        return f'{self.name} moves with four paws'