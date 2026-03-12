from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class Gender(str,Enum):
    male ="male"
    female = "female"
    others = "others"



class Item(BaseModel):
    name : str
    age : int
    classes : int
    gender : Gender | None = None
    Like :bool = True

app = FastAPI()

@app.post("/student/{student_id}")
async def student(student_id:int,item :Item):
    item_dop = item.model_dump()
    item_dop.update({"student_id":student_id})
    return item_dop