from sqlmodel import Session, SQLModel, create_engine, select

sqlite_file_name = "student.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})