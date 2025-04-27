from sqlalchemy.orm import Mapped
from .base import Base

class Answer(Base):
    
    hash_ans: Mapped[str]
    cor_ans: Mapped[str]