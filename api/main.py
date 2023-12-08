from typing import Union

from fastapi.middleware.cors import CORSMiddleware
from fastapi import  FastAPI, Request, Header
from pydantic import BaseModel, Field as PydanticField
from pydantic.fields import Field
# from fastapi import BaseModel
from api.routers import linedb as line_db




app = FastAPI(title="scratch-db", description="connect scratch to database")
app.include_router(line_db.router)



# Root
@app.get("/")
def root():
    return {"title": app.title, "description": app.description}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return item
