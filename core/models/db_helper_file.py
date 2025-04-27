from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from asyncio import current_task
from sqlalchemy.orm import sessionmaker
from core.db_config import settings

class DataBaseHelper():
    def __init__(self, url:str, echo: bool = True):
        self.engine = create_async_engine(
            url = url,
            echo = echo,
        )
        # фабрика по созданию сессий
        self.session_factory = async_sessionmaker(
            bind = self.engine,
            autoflush= False,
            autocommit = False,
            expire_on_commit= False,            
        )
    # Помощник для создания сессии
    # При работе с бд нужн создавать сессии
    def get_scoped_session (self):
        # session - новый объект сессии
        session = async_scoped_session(
            session_factory=self.session_factory,
            # scopefunc -ограниченное пр-во, заданное каким-то параметром
            # curent_task - проверяет на принадлежность к текущей сессии 
            scopefunc=current_task,
        )
        return session
    # метод для создания сессии для каждого запроса
    async def session_dependacy(self) -> AsyncSession:        
        # с  self.get_scoped_session() создается новая сессия
        # с которой будет происходить работа 
        async with self.session_factory() as session:
            # Чтобы сессия не закрывалась
            # вместо return используем генератор - yield, т.к. 
            # yeld возвращает значениея по мере выполнения функции, не останавливая функцию
            yield session
            # Закрытие текущей сессии
            await session.close()

    async def scoped_session_dependacy(self) -> AsyncSession:        
        sesion = self.get_scoped_session()
        yield sesion
        await sesion.close()

db_helper = DataBaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)

# from core.models impore db_helper
# fun(session: AsyncSession= db_helper.session_dependency) 