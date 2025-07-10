from fastapi import FastAPI, status, HTTPException
from SchemaStudent import StudentPublic, StudentSchema, StudentsList

app = FastAPI()

DataBase = []

@app.get("/getStudents", response_model=StudentsList, status_code=status.HTTP_200_OK)
def getStudents():
    if not DataBase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No students found"
        )

    return {'students': DataBase}

@app.post("/addNewStudent", response_model=StudentPublic, status_code=status.HTTP_201_CREATED)
def createStudent(student: StudentSchema) -> StudentPublic:
    
    nonRepeatedLetter = student.first_letter_dont_repeat(student.name)

    newStudent = StudentPublic(
        id=len(DataBase) + 1,
        name=student.name,
        score=student.score,
        nonRepeatedLetter=nonRepeatedLetter
    )

    DataBase.append(newStudent)
    
    return newStudent

@app.put("/updateStudent/{id}", response_model=StudentPublic, status_code=status.HTTP_202_ACCEPTED)
def updateStudent(id: int, new_info: StudentSchema):
    
    if not new_info or new_info is []:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="No information has been added"
            )
    
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
