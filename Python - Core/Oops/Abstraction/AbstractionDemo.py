from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def makeSound(self):
        pass 

class Dog(Animal):
    def makeSound(self):
        print("Bark")

class Cat(Animal):
    def makeSound(self):
        print("Meow")

dog=Dog()
dog.makeSound()