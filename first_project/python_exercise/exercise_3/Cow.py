from first_project.python_exercise.exercise_3.Animal import Animal


class Cow(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "mu"

    def move(self):
        return f'{self.name} moves with four paws'

