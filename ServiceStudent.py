from ModelStudent import Student
from SchemaStudent import first_letter_dont_repeat
from sqlmodel import Session, select, delete, update, insert
from DB import engine

class Student_CRUD():
    def get_students() -> list:
        try:
            with Session(engine) as session:
                return session.exec(select(Student)).all()
            
        except Exception as err:
            session.rollback()
            print(f"erro inesperado: {err}")
                
    def create_students(student: dict) -> dict:
        try:
            student["nonRepeatedLetter:"] = first_letter_dont_repeat(student["name"])
            
            with Session(engine) as session:
                result = session.exec(insert(Student).
                                values(student).
                                returning(Student.id, Student.name, Student.score, Student.firstLetterNotRepetead))
                
                session.commit()
                
                return result.fetchone().asdict
                
        except Exception as err:
            session.rollback()
            print(f"erro inesperado: {err}")