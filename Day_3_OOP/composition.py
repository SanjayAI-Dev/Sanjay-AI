"""#represents a relation in the code 
#strong ownership that destroys the main 

#example-credit card and payment
#Composition has a stronger-relation(stronger HAS-A Relation)
#example  Engine and Car


#Aggregation has a weaker-relation(weaker HAS-A Relation)-----often independent 

#example deptartment and employee

#inheritance vs compostion:
# Parent class
class Vehicle:
    pass


# Engine class
class Engine:
    pass


# Car inherits from Vehicle
class Car(Vehicle):

    def __init__(self):
        # Creating an Engine object inside the Car
        # This represents Composition (HAS-A relationship)
        self.engine = Engine()



"""
#Dundar method Or Magic method
class Student:

    def __init__(self, name, marks):
        # __init__ is called automatically when an object is created
        self.name = name
        self.marks = marks

    def __str__(self):
        # __str__ controls what print(object) displays
        return f"Student: {self.name}, Marks: {self.marks}"

    def __repr__(self):
        # __repr__ gives a developer-friendly representation
        return f"Student('{self.name}', {self.marks})"

    def __len__(self):
        # __len__ allows us to use len(object)
        return len(self.name)

    def __eq__(self, other):
        # __eq__ compares two objects using ==
        return self.marks == other.marks

    def __add__(self, other):
        # __add__ allows us to use + between two objects
        return self.marks + other.marks


student1 = Student("Jaya", 90)
student2 = Student("Rahul", 80)
student3 = Student("Amit", 90)


# __str__
print(student1)

# __repr__
print(repr(student1))

# __len__
print(len(student1))

# __eq__
print(student1 == student2)
print(student1 == student3)

# __add__
print(student1 + student2)