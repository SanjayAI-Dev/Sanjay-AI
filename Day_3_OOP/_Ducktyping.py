class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Hello")


def make_speak(obj):
    obj.speak()


make_speak(Dog())
make_speak(Robot())