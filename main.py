from fastapi import FastAPI

app =FastAPI()

db_hero = {"superhero":"superman"},{"superhero":"batman"},{"superhero":"catwomen"}

@app.get("/hero/")
def superhero(skip:int=0, limit:int=10):
    return db_hero[skip :skip +limit]
