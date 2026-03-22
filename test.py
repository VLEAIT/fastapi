from fastapi import FastAPI,Path,Body 
from pydantic import BaseModel,Field
from typing import Annotated


                

app = FastAPI()


class gun(BaseModel):
    name : str | None = Field(examples=["ak47"],description="the name of  gun you use")
    caliber : str | None = Field(examples=["ak"])
    price : float | None = None
   
   
@app.put("/gun")
async def new_gun(Gun : Annotated[gun,Body(openapi_examples={"normal gun":{"summary":"a normal gun","description":"this is a normal gun","value":{"name":"ak47","caliber":"7.62mm","price":1500.0}},"bad gun":{"summary":"a bad gun","description":"this is a bad gun","value":{"name":"ak47","caliber":"7.62mm"}}})]):
    gun_data = Gun.model_dump()
    return{"message":"gun added","gun":gun_data}   