"""class Car:
    def start(self):
        print("car started")

car = Car()
car.start()
"""
class Car:
    def start(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print