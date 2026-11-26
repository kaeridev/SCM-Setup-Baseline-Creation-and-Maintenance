from fastapi import FastAPI
from models import Student
from services import get_students

app = FastAPI()



@app.get("/students", response_model=list[Student])
def list_students():
    return get_students()