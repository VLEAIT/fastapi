from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
bikes =[]

class Bike(BaseModel):
    name : str
    cc : int
    price : float


@app.post("/query")
async def query_typ(q:Annotated[str | None, Query(min_length=4)],bike:Bike):
    bikes.append(bike.model_dump())
    return{"message":"bikes added","bikes":bikes}

@app.get("/send")
async def get_bike():
    return bikes
 

