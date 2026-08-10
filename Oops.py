"""# 01_Classes.py
class Car:#class
    def start(self,brand,price):
        self.brand =brand
        self.price = price
        print("Car started")

    def display(self):#method
        print(self.brand,self.price)

car_new= Car()#object declare
car_new.start("maruti",2000000) # call the method with object 

car_new.display()#print the data object 
#attribute=method =obj

name -public 
_name ->protected
__name ->private 
"""

class Vechicle:
    def start(self):
        print('vechicle started')

class Car(Vechicle):
    pass
# multi-level inheritance
class Model(Car):
    pass

model =Car()
model.start()
model.start()