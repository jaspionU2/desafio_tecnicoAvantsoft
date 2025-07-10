from typing import Annotated, Optional
from pydantic import BaseModel, Field, model_validator, field_validator

class StudentPublic(BaseModel):  
    id: int
    name: str
    score: Annotated[float, Field(gt=0, le=10)]
    nonRepeatedLetter: str


class StudentSchema(BaseModel):
    name: str
    score: Annotated[float, Field(ge=0, le=10)]
    
    @field_validator('name', mode='after')
    @classmethod
    def first_letter_dont_repeat(cls, value: str) -> str:
        appearanceLetters = {}
        
        for letter in value:
            if letter not in appearanceLetters:
                appearanceLetters[letter] = 0
            appearanceLetters[letter] += 1
    
        non_repetead = [letter for letter, count in appearanceLetters.items() if count == 1]
        
        return non_repetead[0] if non_repetead else '_'
    
class StudentsList(BaseModel):
    students: list[StudentPublic]
        