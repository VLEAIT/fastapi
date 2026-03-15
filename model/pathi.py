from fastapi import FastAPI,Path,Query
from typing import Annotated


app = FastAPI()

@app.get("/Item/{Item_id}")
async def item_name(Item_id : Annotated[int,Path(title="the user id of item")], q:Annotated[str | None,Query(alias="Item_query")] = None,):
    result = {"item_id":Item_id}
    if q:
        result.update({"q":q})
    return result
