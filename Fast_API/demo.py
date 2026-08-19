from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI(title="Pydantic Models Demo")

students_db: dict[int, dict] = {}
next_id = 1


# ---- Nested model ----
class Address(BaseModel):
    city: str
    state: str
    pincode: str = Field(..., min_length=6, max_length=6)


# ---- Model for CREATING a student ----
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: EmailStr
    course: str
    address: Optional[Address] = None   # nested model, optional


# ---- Model for UPDATING a student (all fields optional) ----
class StudentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=50)
    age: Optional[int] = Field(default=None, gt=0, lt=120)
    email: Optional[EmailStr] = None
    course: Optional[str] = None


# ---- Model for RESPONSES (what the client sees back) ----
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    course: str


@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    global next_id
    new_student = student.dict()
    new_student["id"] = next_id
    students_db[next_id] = new_student
    next_id += 1
    return new_student   # extra fields (like "address") are dropped by response_model


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")

    stored = students_db[student_id]
    updates = student.dict(exclude_unset=True)   # only fields the client actually sent
    stored.update(updates)
    students_db[student_id] = stored
    return stored