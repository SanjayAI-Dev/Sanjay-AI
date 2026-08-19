# ============================================================
# FILE: manager.py
# ============================================================
#
# TOPICS COVERED:
# 1. Importing modules
# 2. Multiple imports
# 3. Classes and Objects
# 4. Constructor (__init__)
# 5. Instance variables
# 6. Methods
# 7. self keyword
# 8. Lists
# 9. for loops
# 10. if statements
# 11. Comparison operators
# 12. Object creation
# 13. Custom exceptions
# 14. raise keyword
# 15. File handling
# 16. JSON persistence
# 17. return statement
# 18. List methods
# ============================================================




# ------------------------------------------------------------
# TOPIC: IMPORT
# Import the Student class from student.py
# ------------------------------------------------------------
from student import Student




# ------------------------------------------------------------
# TOPIC: IMPORTING CUSTOM EXCEPTIONS
#
# We import the custom exceptions created in exceptions.py.
#
# StudentNotFoundError
#     → Used when a student does not exist.
#
# DuplicateStudentError
#     → Used when a student ID already exists.
# ------------------------------------------------------------
from exception import (
    StudentNotFoundError,
    DuplicateStudentError
)




# ------------------------------------------------------------
# TOPIC: IMPORTING FUNCTIONS
#
# These functions are responsible for saving and loading
# student data from students.json.
# ------------------------------------------------------------
from file import save_students, load_students




# ============================================================
# CLASS: StudentManager
# ============================================================
#
# This class manages all student operations.
#
# It acts as the "business logic" of the application.
#
# Responsibilities:
#
# - Load students
# - Add students
# - View students
# - Search students
# - Delete students
# ============================================================


class StudentManager:


    # ========================================================
    # CONSTRUCTOR
    # ========================================================
    # __init__ runs automatically when StudentManager object
    # is created.
    # ========================================================


    def __init__(self):


        # ----------------------------------------------------
        # TOPIC: INSTANCE VARIABLE
        #
        # self.students stores all Student objects.
        #
        # Initially, the list is empty.
        # ----------------------------------------------------
        self.students = []


        # ----------------------------------------------------
        # Load existing students from the JSON file.
        # ----------------------------------------------------
        self.load_data()




    # ========================================================
    # METHOD: load_data()
    # ========================================================
    # Purpose:
    # Load students from students.json and convert each
    # dictionary back into a Student object.
    # ========================================================


    def load_data(self):


        # ----------------------------------------------------
        # Call load_students() from file_handler.py
        #
        # Example returned data:
        #
        # [
        #     {
        #         "student_id": 101,
        #         "name": "Rahul",
        #         "age": 20,
        #         "course": "Python",
        #         "marks": 90
        #     }
        # ]
        # ----------------------------------------------------
        data = load_students()




        # ----------------------------------------------------
        # TOPIC: FOR LOOP
        #
        # Process every student dictionary.
        # ----------------------------------------------------
        for item in data:


            # ------------------------------------------------
            # TOPIC: OBJECT CREATION
            #
            # Create a Student object using dictionary data.
            # ------------------------------------------------
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )


            # ------------------------------------------------
            # TOPIC: LIST append()
            #
            # Add the Student object to self.students.
            # ------------------------------------------------
            self.students.append(student)




    # ========================================================
    # METHOD: add_student()
    # ========================================================
    # Purpose:
    # Add a new student to the system.
    # ========================================================


    def add_student(
        self,
        student_id,
        name,
        age,
        course,
        marks
    ):


        # ----------------------------------------------------
        # TOPIC: FOR LOOP
        #
        # Check every existing student.
        # ----------------------------------------------------
        for student in self.students:


            # ------------------------------------------------
            # TOPIC: CONDITIONAL STATEMENT
            #
            # Check whether the new student ID already exists.
            #
            # == means "equal to"
            # ------------------------------------------------
            if student.student_id == student_id:


                # --------------------------------------------
                # TOPIC: CUSTOM EXCEPTION
                #
                # Stop the operation because the ID is already
                # being used.
                #
                # raise manually generates an exception.
                # --------------------------------------------
                raise DuplicateStudentError(
                    "Student ID already exists."
                )




        # ----------------------------------------------------
        # If no duplicate ID was found, create a new Student
        # object.
        # ----------------------------------------------------
        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )




        # ----------------------------------------------------
        # TOPIC: LIST append()
        #
        # Add the new Student object to the list.
        # ----------------------------------------------------
        self.students.append(student)




        # ----------------------------------------------------
        # TOPIC: FILE HANDLING
        #
        # Save updated student data into students.json.
        # ----------------------------------------------------
        save_students(self.students)




        # ----------------------------------------------------
        # Display success message.
        # ----------------------------------------------------
        print("Student added successfully.")




    # ========================================================
    # METHOD: view_students()
    # ========================================================
    # Purpose:
    # Display all students.
    # ========================================================


    def view_students(self):


        # ----------------------------------------------------
        # TOPIC: CONDITIONAL STATEMENT
        #
        # An empty list evaluates to False.
        #
        # Therefore:
        # if not self.students
        #
        # means:
        # "If there are no students..."
        # ----------------------------------------------------
        if not self.students:


            print("No students found.")


            # -----------------------------------------------
            # TOPIC: return
            #
            # Stop the method immediately.
            # -----------------------------------------------
            return




        # ----------------------------------------------------
        # TOPIC: FOR LOOP
        #
        # Loop through all Student objects.
        # ----------------------------------------------------
        for student in self.students:


            # Call the display() method of Student class.
            student.display()




    # ========================================================
    # METHOD: search_student()
    # ========================================================
    # Purpose:
    # Find a student using student_id.
    # ========================================================


    def search_student(self, student_id):


        # ----------------------------------------------------
        # Search through all students.
        # ----------------------------------------------------
        for student in self.students:


            # ------------------------------------------------
            # Check whether the ID matches.
            # ------------------------------------------------
            if student.student_id == student_id:


                # --------------------------------------------
                # Student found.
                # --------------------------------------------
                student.display()


                # Stop searching.
                return




        # ----------------------------------------------------
        # If the loop finishes without finding the student,
        # raise a custom exception.
        # ----------------------------------------------------
        raise StudentNotFoundError(
            "Student not found."
        )




    # ========================================================
    # METHOD: delete_student()
    # ========================================================
    # Purpose:
    # Delete a student using student_id.
    # ========================================================


    def delete_student(self, student_id):


        # ----------------------------------------------------
        # Search for the student.
        # ----------------------------------------------------
        for student in self.students:


            # ------------------------------------------------
            # Check whether the ID matches.
            # ------------------------------------------------
            if student.student_id == student_id:


                # --------------------------------------------
                # TOPIC: LIST remove()
                #
                # Remove the matching Student object.
                # --------------------------------------------
                self.students.remove(student)




                # --------------------------------------------
                # Save the updated list to the JSON file.
                # --------------------------------------------
                save_students(self.students)




                # --------------------------------------------
                # Display success message.
                # --------------------------------------------
                print("Student deleted successfully.")




                # --------------------------------------------
                # Stop the method.
                # --------------------------------------------
                return




        # ----------------------------------------------------
        # Student was not found.
        # ----------------------------------------------------
        raise StudentNotFoundError(
            "Student not found."
        )

