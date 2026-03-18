from fastapi import FastAPI,Query
from typing import Annotated,Literal
from pydantic import BaseModel,Field

app = FastAPI()

class dreambike(BaseModel):
    model_config ={"extra":"forbid"}
    name: str = Field(description="tell your fav bike name")
    cc :int =Field(400,gt=150,le=500,description="tell your fave bike cc")
    price:float =Field(description="tell your fav bike price")
    bought :Literal["yes","No"] = "No"
    b_bikes :list[str] = Field(description="tell your best bikes")

@app.post("/bikes")
async def bikes_name(bikes_s : dreambike):
    if bikes_s.bought == "yes":
        return{"message":"your dream bike is added","bikes":bikes_s.model_dump()}

@app.get("/get_my bikes")
async def get_bikes(*,bikes_s : Annotated[dreambike, Query()],q :str):
    if bikes_s.name == "hunter":
        return bikes_s
