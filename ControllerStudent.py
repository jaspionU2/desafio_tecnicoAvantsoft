from fastapi import APIRouter, status, Response, HTTPException
from fastapi.responses import JSONResponse
from SchemaStudent import StudentPublic, StudentSchema, StudentsList
from ServiceStudent import first_letter_dont_repeat, Student_CRUD

router_student = APIRouter()

@router_student.get("/getStudents", response_model=StudentsList)
def list_students(response: Response):
    students_list = StudentsList
    students_list.students = Student_CRUD.get_students()
    
    if students_list is None or not students_list.students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Students not found"
        )   
    
    response.status_code = status.HTTP_200_OK
    return students_list

@router_student.get("/getStudentsById/{student_id}", response_model=StudentPublic)
def get_student(student_id: int, response: Response) -> StudentPublic:
    student = Student_CRUD.get_student_by_id(student_id)
    
    if student is None or not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    
    response.status_code = status.HTTP_200_OK
    return student

@router_student.post("/createStudent", response_model=StudentPublic)
def create_student(student_data: StudentSchema, response: Response) -> StudentPublic:
    if not student_data or student_data is {}:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )
        
    first_letter = first_letter_dont_repeat(student_data.name)  
    student_dict = student_data.model_dump()
    student_dict["firstLetter"] = first_letter
    
    created_student = Student_CRUD.create_students(student_dict)
    
    if not created_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    response.status_code = status.HTTP_201_CREATED
    return created_student

@router_student.put("/updateStudent/{student_id}", response_model=StudentPublic)
def update_student(student_id: int, student_data: StudentSchema, response: Response):
    if not student_data or student_data is {}:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )
        
    first_letter = first_letter_dont_repeat(student_data.name)  
    student_dict = student_data.model_dump()
    student_dict["firstLetter"] = first_letter
    
    updated_student = Student_CRUD.update_student(student_id, student_dict)
    
    if not updated_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    response.status_code = status.HTTP_200_OK
    return updated_student
    
@router_student.delete("/deleteStudent/{student_id}")
def delete_student(student_id: int, response: Response):
    deleted = Student_CRUD.delete_student(student_id)
    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not delete the specified student"
        )
    
    response.status_code = status.HTTP_200_OK
    return JSONResponse("Student deleted successfully", status_code=status.HTTP_200_OK)
