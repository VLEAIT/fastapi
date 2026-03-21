from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import BaseModel
from enum import Enum

app = FastAPI()
bikes =[]
class type(BaseModel):
    classic = "classic"
    sports = "sports"
    caferacer = "caferacer"

class rpm(str,Enum):
    low = "low"
    medium = "medium"
    high = "high"
class Bike(BaseModel):
    name : str
    cc : int
    price : float | None = None
    types : type
    owner :set[str] = set()
    Rpm : rpm



@app.get("/query")
async def query_typ(q:Annotated[str | None, Query(min_length=4)],bike:Bike):
    bikes.append(bike.model_dump())
    return{"message":"bikes added","bikes":bikes}

@app.get("/send")
async def get_bike():
    return bikes
 

