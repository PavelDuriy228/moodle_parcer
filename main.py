import asyncio
from typing import Annotated
from contextlib import asynccontextmanager
from core.models import db_helper, Base
from sqlalchemy.ext.asyncio import AsyncSession
from db_funcs.crud import create_answer
from db_funcs.schemas import CreateAnswer

# @asynccontextmanager
async def lifespan():
    async with db_helper.engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)
    # yield


async def main():
    # await lifespan()
    new_asn = CreateAnswer(
        hash_ans='erc',
        cor_ans= "dsd"
    )
    print(new_asn)
    
    # ПРимер выполненния запросов к БД
    # async with db_helper.session_factory() as session:
    #     await create_answer(
    #         session=session,
    #         answer_in=new_asn
    #     )

if __name__=="__main__":
    asyncio.run(main())