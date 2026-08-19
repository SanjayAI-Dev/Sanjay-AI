from Students import Student
from exception import DuplicateStudentError,StudentNotFoundError
from file import save_students,load_students

class StudentMain:
    def __init__(self):
        self.students=[]
        self.load_data()

    def load_data(self):
        data=load_students()
        for item in data:
            student=Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
                        )

        self.students.append(student)
      

    def add_student(self,student_id,name,age,course,marks):
        for student in self.students:
            if student==student_id:
                raise DuplicateStudentError("Student is already present")
            
            student=student(student_id,name,age,course,marks)
            self.students.append(student)
            save_students(self.students)
            print("student added sucessfully")

    def view_students(self):
        if not self.students:
            print("no student found")
            return
        for student in self.students():
            student.display()

    def search_student(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                student.display()
                return
        raise StudentNotFoundError("student not found")

    def delete_student(self,student_id):
        for student in self.students:
            if student.student_id==student_id:
                self.student.remove(student)
                save_students(self.students)
        raise StudentNotFoundError("student not found")
    
            


        

    



                
