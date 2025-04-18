from abc import ABC


class Car(ABC):

    def move(self):
        return "is moving"

    def turn_on(self):
        return "started"
