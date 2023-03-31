from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

from config import settings


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


if __name__ == '__main__':
    engine = create_engine(str(settings.db_url), echo=True)

    SQLModel.metadata.create_all(engine)
