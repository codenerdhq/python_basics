class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    @staticmethod
    def print_total_cars():
        print(f"Total cars: {Car.total_cars}")


# Use the static method
Car.print_total_cars()
# User the class method
print("Total cars:", Car.get_total_cars())

car1 = Car()
car2 = Car()

# Use the static method
Car.print_total_cars()
# User the class method
print("Total cars:", Car.get_total_cars())
