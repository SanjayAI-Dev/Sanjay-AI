class Student:
    def __init__(self,student_id,name,age,course,marks):
        self.student_id= student_id
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks

        pass
    def CalculateGrade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=80:
            return "B"
        elif self.marks>=70:
            return "C"
        elif self.marks>=60:
            return "D"
        else:
            return "F"

    def To_Dict(self):
        return{
               "student_id":self.student_id,
               "name":self.name,
               "age":self.age,
               "course":self.course,
               "marks":self.marks,
               "grade":self.CalculateGrade()
               }

    def Display(self):
        print(f"student_id: {self.student_id}\n" )
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"course: {self.course}")
        print(f"marks: {self.marks}")

student1=Student(
        101,"sanjay",22,"python",92
    )    
student2=Student(
        102,"jay",24,"java",85
    )
student3=Student(
        103,"raghu",23,"JS",70
    )

student1.Display()
print(f"student1 : ",student1.CalculateGrade())
student2.Display()
print(f"student2 : ",student2.CalculateGrade())
student3.Display()
print(f"student3 : ",student3.CalculateGrade())

print("student dictionary")
student_data1=student1.To_Dict()
student_data2=student2.To_Dict()
student_data3=student3.To_Dict()
print(Student)
print(student_data1)
print(student_data2)
print(student_data3)