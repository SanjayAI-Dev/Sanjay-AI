from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Error Handling Demo")

students_db = {1: {"id": 1, "name": "Aditi Sharma", "age": 21, "course": "Python"}}
fake_tokens = {"valid-token": {"username": "aditi", "role": "student"}}


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str


# ---- Custom exception type ----
class DuplicateStudentError(Exception):
    def __init__(self, name: str):
        self.name = name


# ---- Global handler for the custom exception ----
@app.exception_handler(DuplicateStudentError)
def handle_duplicate_student(request: Request, exc: DuplicateStudentError):
    return JSONResponse(
        status_code=400,
        content={"detail": f"A student named '{exc.name}' already exists"},
    )


# ---- 404 Not Found ----
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]


# ---- 401 Unauthorized ----
@app.get("/profile")
def profile(token: str):
    if token not in fake_tokens:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return fake_tokens[token]


# ---- 403 Forbidden ----
@app.delete("/students/{student_id}")
def delete_student(student_id: int, token: str):
    user = fake_tokens.get(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete students")
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[student_id]
    return {"message": "Student deleted"}


# ---- 400 Bad Request (via custom exception) ----
@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    for existing in students_db.values():
        if existing["name"].lower() == student.name.lower():
            raise DuplicateStudentError(student.name)
    new_id = max(students_db.keys(), default=0) + 1
    new_student = student.dict()
    new_student["id"] = new_id
    students_db[new_id] = new_student
    return new_student


# ---- 500 Internal Server Error (unhandled bug, for illustration only) ----
@app.get("/broken")
def broken_endpoint():
    return 1 / 0   # deliberately raises ZeroDivisionError -> FastAPI returns a generic 500

