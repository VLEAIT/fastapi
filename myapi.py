from fastapi import FastAPI

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
def get_herione(student_id: int):
    return(students[student_id])
