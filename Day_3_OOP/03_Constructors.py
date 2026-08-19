# 03_Constructors

"""method automatically called when created an object
    its used __
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
