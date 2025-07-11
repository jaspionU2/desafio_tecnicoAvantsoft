from sqlmodel import SQLModel, create_engine
from ModelStudent import Student

sqlite_file_name = "student.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False}, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)


