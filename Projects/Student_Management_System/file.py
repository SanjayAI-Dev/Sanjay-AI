import json
FILE_NAME="students.json"

def save_students(students):
    data=[]

    for student in students:
        data.append(student.To_Dict())

    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent=4)


def load_students(students):
    try:
        with open(FILE_NAME,"r") as file:
             return json.load(file)
            
    
    except FileNotFoundError:
        return[]
    
