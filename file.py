# ============================================================
# TOPIC: FILE HANDLING + JSON
# ============================================================
# This module is responsible for:
#
# 1. Saving student data into a JSON file
# 2. Loading student data from a JSON file
# 3. Handling FileNotFoundError
# 4. Working with lists and dictionaries
# 5. Using functions
# 6. Using loops
# 7. Using the with statement
# ============================================================


# ------------------------------------------------------------
# TOPIC: Importing a Module
# json is Python's built-in module for working with JSON data.
# ------------------------------------------------------------
import json


# ------------------------------------------------------------
# TOPIC: Constant
# The file name is stored in a variable.
#
# By convention, constants are written in UPPERCASE.
# ------------------------------------------------------------
FILE_NAME = "students.json"


# ============================================================
# FUNCTION: save_students()
# ============================================================
# Purpose:
# Save all students into students.json
#
# Topics covered:
# - Functions
# - Lists
# - for loop
# - Object methods
# - Dictionary
# - File handling
# - JSON
# ============================================================

def save_students(students):

    # --------------------------------------------------------
    # Create an empty list.
    #
    # This list will store student dictionaries.
    # --------------------------------------------------------
    data = []

    # --------------------------------------------------------
    # TOPIC: for loop
    #
    # Loop through every Student object.
    # --------------------------------------------------------
    for student in students:

        # ----------------------------------------------------
        # TOPIC: Method Calling
        #
        # to_dict() converts the Student object into
        # a dictionary.
        #
        # Example:
        #
        # Student object
        #       ↓
        #     to_dict()
        #       ↓
        # Dictionary
        # ----------------------------------------------------
        data.append(student.to_dict())

    # --------------------------------------------------------
    # TOPIC: File Handling
    #
    # "w" = write mode
    #
    # If the file doesn't exist:
    #     Python creates it.
    #
    # If the file already exists:
    #     Its previous content is replaced.
    # --------------------------------------------------------
    with open(FILE_NAME, "w") as file:

        # ----------------------------------------------------
        # TOPIC: JSON
        #
        # json.dump() converts Python data into JSON
        # and writes it into the file.
        #
        # indent=4 makes the JSON file readable.
        # ----------------------------------------------------
        json.dump(data, file, indent=4)


# ============================================================
# FUNCTION: load_students()
# ============================================================
# Purpose:
# Read student data from students.json
#
# Topics covered:
# - Functions
# - File handling
# - JSON
# - try/except
# - FileNotFoundError
# - return statement
# ============================================================

def load_students():

    # --------------------------------------------------------
    # TOPIC: Exception Handling
    #
    # try contains code that might produce an error.
    # --------------------------------------------------------
    try:

        # ----------------------------------------------------
        # TOPIC: File Handling
        #
        # "r" = read mode
        # ----------------------------------------------------
        with open(FILE_NAME, "r") as file:

            # ------------------------------------------------
            # TOPIC: JSON
            #
            # json.l




return json.load(file)

    # --------------------------------------------------------
    # TOPIC: Custom Error Handling
    #
    # FileNotFoundError occurs when students.json
    # does not exist.
    # --------------------------------------------------------
    except FileNotFoundError:

        # ----------------------------------------------------
        # If there is no file yet, return an empty list.
        #
        # This prevents the program from crashing.
        # ----------------------------------------------------
        return []