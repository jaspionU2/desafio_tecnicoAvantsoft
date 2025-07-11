from ModelStudent import Student
from sqlmodel import Session, select, delete, update, insert
from DB import engine

def first_letter_dont_repeat(value: str) -> str:
    appearanceLetters = {}
    
    for letter in value.lower():
        if letter not in appearanceLetters:
            appearanceLetters[letter] = 0
        appearanceLetters[letter] += 1

    non_repetead = [letter for letter, count in appearanceLetters.items() if count == 1]
    
    return non_repetead[0] if non_repetead else '_'

class Student_CRUD():

    def get_students():
        try:
            with Session(engine) as session:
                return session.exec(select(Student)).all()
            
        except Exception as err:
            session.rollback()
            print(f"erro inesperado: {err}")
                
    def create_students(student: dict) -> dict:
        try:            
            with Session(engine) as session:
                result = session.exec(
                    insert(Student)
                    .values(student)
                    .returning(Student.id, Student.name, Student.score, Student.firstLetter)
                ).first()
                session.commit()
            if result:
                return dict(result._mapping)
            else:
                return None
        except Exception as err:
            print(f"erro inesperado: {err}")
            return None
