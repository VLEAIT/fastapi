from fastapi import FastAPI,Path
from enum import Enum

class Super_hero(str,Enum):
    superman = "superman"
    batman ="batman"
    catwomen ="catwomen"

app =FastAPI()


@app.get("/super/{sup_hero}")
async def super_her(sup_hero:Super_hero=Path(description="The name of superhero option")):
    if sup_hero is Super_hero.superman:
        return{"sup_hero":sup_hero,"message":"the hero is here"}
    if sup_hero.value =="batman":
         return{"sup_hero":sup_hero,"message":"the hero is here"}
       
    return{"sup_hero":sup_hero,"message":"hero is not in trio"}