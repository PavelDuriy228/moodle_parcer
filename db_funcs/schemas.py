from pydantic import BaseModel, ConfigDict

class AnswersBase(BaseModel):

    hash_ans: str
    cor_ans: str

class CreateAnswer(AnswersBase):
    pass

class Answer(AnswersBase):
    # Переводит атрибуты в ключи
    model_config = ConfigDict(from_attributes=True)

    id : int