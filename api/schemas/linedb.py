from pydantic import  BaseModel, Field

class LineDbBase(BaseModel):
    user_id: str
    message: str

class GetMessage(LineDbBase):
    pass

class FilterUser(BaseModel):
    user_id: str

class ResponseGetMessage(LineDbBase):
    class Config:
        orm_mode = True