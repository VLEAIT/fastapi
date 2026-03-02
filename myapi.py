from fastapi import FastAPI,Path
from typing import Optional

app =FastAPI()

students = {
    1:{
        "name":"hero",
        "age":17,
        "game":"chess"
    }
}
   

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