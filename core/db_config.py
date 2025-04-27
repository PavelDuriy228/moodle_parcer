from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BaseDir = Path(__file__).parent.parent

DB_PATH = BaseDir / "db.sqlite3"

class DbSettings(BaseModel):
    url: str= f"sqlite+aiosqlite:///{DB_PATH}"
    # db_echo - cообщает
    # о всех действиях с БД, когда True
    echo: bool = True


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DbSettings = DbSettings()

settings = Setting()
