from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


# Concrete Classes
class Bird(Animal, Flyable):
    def speak(self):
        return "Chirp"

    def fly(self):
        return "Flying high"

bird = Bird()
print(bird.speak())    # Output: Chirp
print(bird.fly())      # Output: Flying high