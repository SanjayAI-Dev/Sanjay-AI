import os

# ===========================================================
# AI Bootcamp Folder Structure
# ===========================================================

structure = {

    "Day_1_Python_Basics": [
        "01_Comments_and_Print.py",
        "02_Variables.py",
        "03_Data_Types.py",
        "04_Operators.py",
        "05_Input_Output.py",
        "06_F_Strings.py",
        "07_Type_Casting.py",
        "08_All_Basics.py"
    ],

    "Day_2_Control_Flow": [
        "01_Conditional_Statements.py",
        "02_Loops.py",
        "03_Functions.py",
        "04_Data_Structures.py",
        "05_Practice.py"
    ],

    "Day_3_OOP": [
        "01_Classes.py",
        "02_Objects.py",
        "03_Constructors.py",
        "04_Instance_Variables.py",
        "05_Class_Variables.py",
        "06_Instance_Methods.py",
        "07_Class_Methods.py",
        "08_Static_Methods.py",
        "09_Inheritance.py",
        "10_Multiple_Inheritance.py",
        "11_Multilevel_Inheritance.py",
        "12_Hierarchical_Inheritance.py",
        "13_Polymorphism.py",
        "14_Method_Overriding.py",
        "15_Abstraction.py",
        "16_Encapsulation.py",
        "17_Practice.py"
    ],

    "Day_4_Exception_Handling": [
        "01_Try_Except.py",
        "02_Else_Finally.py",
        "03_Raising_Exceptions.py",
        "04_Custom_Exceptions.py",
        "05_Practice.py"
    ],

    "Day_5_File_Handling": [
        "01_Open_File.py",
        "02_Read_File.py",
        "03_Write_File.py",
        "04_Append_File.py",
        "05_With_Statement.py",
        "06_File_Pointer.py",
        "07_OS_Module.py",
        "08_Practice.py"
    ],

    "Day_6_Git_GitHub": [
        "01_Git_Basics.md",
        "02_Git_Commands.md",
        "03_GitHub_Basics.md",
        "04_Branches.md",
        "05_Merge.md",
        "06_Pull_Request.md",
        "07_Git_Ignore.md",
        "08_GitHub_Workflow.md",
        "09_Practice.md"
    ]
}

# ===========================================================
# Projects
# ===========================================================

projects = [
    "Calculator",
    "Student_Management_System",
    "AI_Assistant"
]

# ===========================================================
# Create Day Folders and Files
# ===========================================================

for folder, files in structure.items():

    os.makedirs(folder, exist_ok=True)

    for file in files:

        path = os.path.join(folder, file)

        if not os.path.exists(path):

            with open(path, "w", encoding="utf-8") as f:

                if file.endswith(".py"):
                    f.write(f"# {file.replace('.py', '')}\n")

                elif file.endswith(".md"):
                    title = file.replace(".md", "").replace("_", " ")
                    f.write(f"# {title}\n")

# ===========================================================
# Create Project Folders
# ===========================================================

os.makedirs("Projects", exist_ok=True)

for project in projects:
    os.makedirs(os.path.join("Projects", project), exist_ok=True)

# ===========================================================
# Success Message
# ===========================================================

print("=" * 60)
print("✅ AI Bootcamp Folder Structure Created Successfully!")
print("=" * 60)