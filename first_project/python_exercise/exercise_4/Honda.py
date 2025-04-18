from first_project.python_exercise.exercise_4.Car import Car


class Honda(Car):
    def __init__(self, name):
        self.name = name
        self.ignition = False

    def move(self):
        self.ignition = True
        print("the car is moving")


    def turn_on(self):
        self.ignition = True
        print("The car is turned on")


