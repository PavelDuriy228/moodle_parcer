from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, declared_attr

# Базовый класс для описания моделей (работы с ОРМ)
class Base(DeclarativeBase):
    # Чтобы эта модель не создавалась в БД
    # Мы указываем что эта модель - абстрактная
    __abstract__ = True
    # Эта функция автоматически
    # создает таблицу, равную названию
    # класса (модели)  
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
    id: Mapped[int] = mapped_column(primary_key=True)