from fastapi import FastAPI,Body
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Literal,Any
app = FastAPI()
class games(BaseModel):
    name : str | None = Field(None,examples=["chess"],description="the name of  game you play")
    types : str | None = Field(None,examples=["board game"])
    price : float | None = None
    genre : list[str]=[]
    like : bool | None = None
    rate :Literal[1,2,3,4,5] = 5
    email : EmailStr | None = None

game_db : list[games] = [
    {"name":"witcher 3",
     "types":"rpg",
     "price":50.0,
     "genre":["action","adventure"],
     "like":True,
     "rate":5,
     "email":"witcher3@example.com"
    },
    {"name":"bad game",
     "types":"unknown",
     "price":None,
     "genre":[],
     "like":None,
     "rate":5,
     "email":None
    }
]



@app.get("/game",response_model=list[games])
async def get_game():
    return game_db

@app.post("/game",response_model=games)
async def new_game(Game : Annotated[games,Body(openapi_examples={"rpg games":{"summary":"a rpg game","description":"this is a rpg game","value":{"name":"witcher 3","types":"rpg","price":50.0,"genre":["action","adventure"],"like":True,"rate":5,"email":"witcher3@example.com"}},"battle ground":{"summary":"a battle ground game","description":"this is a battle ground game","value":{"name":"bad game","types":"unknown","email":None}}})]) ->Any:
    game_db.append(Game.model_dump())
    return Game

@app.put("/game/{game_id}",response_model=games)
async def update_game(game_name:str,Game : Annotated[games,Body(openapi_examples={"rpg games":{"summary":"a rpg game","description":"this is a rpg game","value":{"name":"witcher 3","types":"rpg","price":50.0,"genre":["action","adventure"],"like":True,"rate":5,"email":"witcher3@example.com"}},"battle ground":{"summary":"a battle ground game","description":"this is a battle ground game","value":{"name":"bad game","types":"unknown","email":None}}})]) -> Any:
    for i,g in enumerate(game_db):
        if g["name"]==game_name:
            game_db[i] = Game.model_dump()
            return Game
    return {"message":"game not found"}

@app.delete("/game/{game_id}")
async def delete_game(game_name:str):     
    for i,g in enumerate(game_db):
        if g["name"]==game_name:
            del game_db[i]
            return {"message":"game deleted"}
    return {"message":"game not found"}