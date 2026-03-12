from fastapi import FastAPI,Path
from enum import Enum

class Super_hero(str,Enum): #create options in drop down
    superman = "superman"
    batman ="batman"
    catwomen ="catwomen"

app =FastAPI()


@app.get("/super/{sup_hero}")
async def super_her(sup_hero:Super_hero=Path(description="The name of superhero option")):
    messages ={
        Super_hero.superman :{"message":"the hero is is alien","power":"he can fly"},
        Super_hero.batman :{"message":"thr hero is orfan ","power":"he is rich"},
        Super_hero.catwomen:{"message":"the hero is thief","power":"she is flexible"}
        }
    
    if sup_hero is Super_hero.superman:
        return{"super_hero":sup_hero , **messages[sup_hero]}
    if sup_hero is Super_hero.batman:
        return{"super_hero":sup_hero,**messages[sup_hero]}
    if sup_hero is Super_hero.catwomen:
        return{"super_hero":sup_hero,**messages[sup_hero]}
    

@app.get("/hero")
async def hero_name(*,name : str ,surname: str, power:str |None =None , dance : bool =False):
    sakar ={"name":name,"surname":surname}
    if power:
        sakar.update({"power":power})

    return sakar
       
    
