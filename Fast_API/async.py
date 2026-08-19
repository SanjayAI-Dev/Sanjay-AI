import asyncio
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Async Endpoints Demo")

students_db = {
    1: {"id": 1, "name": "Aditi Sharma", "age": 21, "course": "Python"},
    2: {"id": 2, "name": "Rohan Verma", "age": 22, "course": "FastAPI"},
}


# ---- Simulated async database call (I/O-bound) ----
async def fetch_student_from_db(student_id: int):
    await asyncio.sleep(0.5)   # simulates real network/database latency
    return students_db.get(student_id)


# ---- Async route using the async "database" ----
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    student = await fetch_student_from_db(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# ---- Synchronous route for comparison (FastAPI runs this in a thread pool) ----
@app.get("/students-sync/{student_id}")
def get_student_sync(student_id: int):
    import time
    time.sleep(0.5)   # blocking sleep — simulates a slow synchronous call
    student = students_db.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# ---- Running multiple async operations concurrently ----
@app.get("/students-batch")
async def get_students_batch(ids: str):
    # ids like "1,2" — fetch both students concurrently instead of one after another
    student_ids = [int(i) for i in ids.split(",")]
    results = await asyncio.gather(*(fetch_student_from_db(sid) for sid in student_ids))
    return {"results": [r for r in results if r is not None]}
