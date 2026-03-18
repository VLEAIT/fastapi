from fastapi import FastAPI,Query,Path
from typing import Literal,Annoated
from pydantic import BaseModel,Field


app = FastAPI()

class npk(BaseModel):
    plant : str = Field(description="tell plant name")
    nitrogen : int = Field(120,gt=80,le=200,description="tell nitrogen quantity")
    phosphorus : int = Field(80,gt=50,le=150,description="tell phosphorus quantity")
    potassium : int = Field(100,gt=70,le=180,description="tell potasssium quantitty")
    fertilizer1 : Literal["urea","dap","mop"] = Field(description="tell your fertilizer", default="urea")
    fertilizer2 : Literal["urea","dap","mop"] = Field(description="tell your fertilizer", default="dap")
    fertilizer3 : Literal["urea","dap","mop"] = Field(description="tell your fertilizer", default="mop")
    amount : list[int] = []

class datanpk(BaseModel):
    name : str | None = None
    game :str | None =None
    classe:int
@app.post("/npk")
async def npk_kc(chem: npk):
    return chem



@app.put("/data/{data_id}")
async def neps(*,data_id:Annoated[str ,Path(description="the name is",gt=1)], q:str | None=None,dat:datanpk):
    item =dat.model_dump()
    if data_id:
        item.update({"data_id":data_id})
    return item