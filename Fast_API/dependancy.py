from fastapi import FastAPI, Depends

app = FastAPI()

def get_greeting():
    return "Hello"

@app.get("/greet")
def greet(greeting: str = Depends(get_greeting)):
    return {"message": f"{greeting}, World!"}

