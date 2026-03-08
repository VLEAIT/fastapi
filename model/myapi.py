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

class UpdateStudent(BaseModel):
    name : Optional[str] =None
    age : Optional[int] =None
    game:Optional[str] =None


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



@app.put("/update_student/{student_id}")
def update_student(*,student_id :int=Path(description="ID of student"),student:UpdateStudent):
    if student_id not in students:
       return{"error":"file doesnot exist"}
    if student.name != None:
        students[student_id].name =student.name
    if student.age != None:
        students[student_id].age =student.age
    if student.game !=None:
        students[student_id].game =student.game
        
    return students[student_id]

@app.delete("/delete_student/{student_id}")
def delete_student(student_id:int=Path(description="id of user to del")):
    if student_id not in students:
        return{"error":"the problem is you"}
    
    del students[student_id]
    return("delted succesfully")