from typing import Annotated
from pydantic import BaseModel, Field

class StudentPublic(BaseModel):  
    id: int
    name: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-ZÀ-ü\s]+$')]
    score: Annotated[float, Field(gt=0, le=10)]
    firstLetter: str

class StudentSchema(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-ZÀ-ü\s]+$', examples=['Pablo', 'Anna', 'Josenilson'])]
    score: Annotated[float, Field(ge=0, le=10)]
    

class StudentsList(BaseModel):
    students: list[StudentPublic]
        