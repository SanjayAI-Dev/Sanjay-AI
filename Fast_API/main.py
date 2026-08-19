"""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is a web framework"}"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Student REST API")

# ---- In-memory "database" ----
students_db = {}
next_id = 1


# ---- Data model for creating/updating a student ----
class Student(BaseModel):
    name: str
    age: int
    email: str
    course: str

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: str | None = None
    course: str | None = None

# ---- GET all students ----
@app.get("/students")
def get_all_students():
    return students_db


# ---- GET a single student ----
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]


# ---- POST create a student ----
@app.post("/students", status_code=201)
def create_student(student: Student):
    global next_id
    students_db[next_id] = student.dict()
    students_db[next_id]["id"] = next_id
    created = students_db[next_id]
    next_id += 1
    return created


# ---- PUT update a student ----
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    updated = student.dict()
    
    updated["id"] = student_id
    students_db[student_id] = updated
    return updated


# ---- DELETE a student ----
@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return None

# ---------------- PATCH (Partial Update) ----------------
@app.patch("/students/{student_id}", status_code=200)
def patch_student(student_id: int, student: StudentUpdate):

    if student_id not in students_db:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Get only fields sent by the client
    update_data = student.model_dump(exclude_unset=True)

    # Update only those fields
    students_db[student_id].update(update_data)

    return students_db[student_id]