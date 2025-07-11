from typing import Annotated
from pydantic import BaseModel, Field

class StudentPublic(BaseModel):  
    id: int
    name: Annotated[str, Field(min_length=3, max_length=100, pattern='^[a-zA-ZÀ-ü\s]+$')]
    score: Annotated[float, Field(gt=0, le=10)]
    nonRepeatedLetter: str

class StudentSchema(BaseModel):
    name: Annotated[str, Field(min_length=3, pattern='^[a-zA-ZÀ-ü\s]+$')]
    score: Annotated[float, Field(ge=0, le=10)]
    
def first_letter_dont_repeat(value: str) -> str:
    appearanceLetters = {}
    
    for letter in value:
        if letter not in appearanceLetters:
            appearanceLetters[letter] = 0
        appearanceLetters[letter] += 1

    non_repetead = [letter for letter, count in appearanceLetters.items() if count == 1]
    
    return non_repetead[0] if non_repetead else '_'

class StudentsList(BaseModel):
    students: list[StudentPublic]
        