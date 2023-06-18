# Example 1 of method overriding, 

class Animal:
    def make_sound(self):
        print("I make a sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Dog(Animal):
    pass

animal1 = Animal()
animal1.make_sound()

animal2 = Cat()
animal2.make_sound()

animal3 = Dog()
animal3.make_sound()