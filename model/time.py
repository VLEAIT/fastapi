from fastapi import FastAPI,Body,Cookie
from datetime import datetime,time,timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()

@app.put("/time/{id}")
async def get_time(
    id:UUID,
    user_id:Annotated[str,Cookie()],
    Start_time:Annotated[datetime,Body()],
    process_time:Annotated[timedelta,Body()],
    dead_time:Annotated[timedelta,Body()],
    repeat_time:Annotated[time | None,Body()]
    ):
    start_Time = Start_time + process_time
    end_time =start_Time -dead_time
    return{
        "id":id,
        "start_time":start_Time,
        "end_time":end_time,
        "repeat_time":repeat_time
    }