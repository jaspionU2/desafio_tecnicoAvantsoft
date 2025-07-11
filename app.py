from fastapi import FastAPI
from DB import create_db
from ControllerStudent import router_student

app = FastAPI()

app.include_router(router_student, prefix="/student")

if __name__ == "__main__":
    create_db()
    
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
