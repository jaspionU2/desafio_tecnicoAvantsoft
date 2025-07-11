from sqlmodel import Field, SQLModel

class Student(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    name:  str = Field(index=True)
    score: float = Field(default=None, index=True)
    firstLetter: str | None = Field(default=None)