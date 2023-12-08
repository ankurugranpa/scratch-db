from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import  false
from sqlalchemy.engine import  Result

import api.models.linedb as line_model
import  api.schemas.linedb as line_schema


from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result



async def add_message(
    db: AsyncSession, line_get_message: line_schema.GetMessage
) -> line_model.Message:
    message =line_model.Message(**line_get_message.dict())
    message.send =0
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message

async  def response_get_message(db: AsyncSession):
    message: Result = await (
        db.execute(
            select(
                line_model.Message.user_id,
                line_model.Message.message
            ).filter(line_model.Message.send == false())
        )
    )
    return message.all()