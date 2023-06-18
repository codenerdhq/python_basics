from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started")

# Same as Java Abstract classes 
# cannot be instantiated directly
# This is an error
# vehicle = Vehicle()
# vehicle.start()

car = Car()
car.start()

motorcycle = Motorcycle()
motorcycle.start()
