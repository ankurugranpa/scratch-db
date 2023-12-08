from fastapi import  APIRouter, Depends
import api.schemas.linedb as line_db_schema
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.cruds.linedb as line_db_crud
from  typing import  List
from  time import  sleep

router =APIRouter()

@router.post("/line-db/test", response_model=line_db_schema.GetMessage)
async def get_message(line_body: line_db_schema.GetMessage, db:AsyncSession=Depends(get_db)):
    return  await line_db_crud.add_message(db, line_body)


@router.post("/line-db/get", response_model=List[line_db_schema.ResponseGetMessage])
async  def response_get_message(user_id: line_db_schema.FilterUser ,db: AsyncSession =Depends(get_db)):
    return await line_db_crud.response_get_message(user_id, db)