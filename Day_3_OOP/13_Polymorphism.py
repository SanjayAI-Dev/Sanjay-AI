# 13_Polymorphism
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()