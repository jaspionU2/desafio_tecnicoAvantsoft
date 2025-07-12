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
            
    def get_student_by_id(id: int):
        try:
            with Session(engine) as session:
                return session.exec(select(Student).
                                    where(Student.id == id)).first()
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
        
    def update_student(id: int, student: dict) -> dict:
        try:
            with Session(engine) as session:
                result = session.exec(update(Student).
                             where(Student.id == id).
                             values(student).
                             returning(Student.id, Student.name, Student.score, Student.firstLetter)).first()
                session.commit()
                if result:
                    return dict(result._mapping)
                else:
                    return None
        except Exception as err:
            print(f"erro inesperado: {err}")
            return None
    def delete_student(id: int) -> None | bool:
        try:
            with Session(engine) as session:
                result = session.exec(delete(Student).
                                      where(Student.id == id))
                session.commit()
                return result.rowcount > 0
        except Exception as err:
            print(f"erro inesperado: {err}")
            return None
        
