from sqlmodel import Field, SQLModel

class Student(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    name:  str = Field(index=True)
    score: int = Field(default=0, index=True)
    firstLetterNotRepetead: str = Field(default=None)