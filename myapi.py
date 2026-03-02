from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app =FastAPI()

students = {
    1:{
        "name":"hero",
        "age":17,
        "game":"chess"
    }
}

class Student(BaseModel):
    name :str
    age : int
    game : str

@app.get("/")
def index():
    return("hero")


@app.get("/get-hero/{student_id}")
def get_herione(student_id: int = Path(description="ID number of hero ", gt=0,le=3)):
    return(students[student_id])

@app.get("/get_herodata/{student_id}")
def get_studentsname(*,student_id:int =Path(description="students id and it value",gt=0),name : Optional[str]= None,type :int):
    for student_id in  students:
        if students[student_id]["name"]==name:
            return(students[student_id])
    return{"name":"no valid"}


@app.post("/get_students/{student_id}")
def get_students(student_id:int, student:Student):
    if student_id in students:
        return{"data":"exists"}
    students[student_id] = student
    return{students[student_id]}