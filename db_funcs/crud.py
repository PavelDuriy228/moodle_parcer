from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Answer

from .schemas import CreateAnswer

# получение всех
async def get_answers(
    session: AsyncSession
)->list[Answer]:
    stat = select(Answer).order_by(Answer.id)
    result:  Result = await session.execute(stat)
    answers = result.scalars().all()
    return list(answers)

async def get_asnwer(
    session: AsyncSession,
    answer_hash: str
)->Answer|None:
    return await session.get(Answer, answer_hash)

async def create_answer(
    session: AsyncSession,
    answer_in: CreateAnswer
):
    ans = Answer(**answer_in.model_dump())
    session.add(ans)    
    await session.commit()
    