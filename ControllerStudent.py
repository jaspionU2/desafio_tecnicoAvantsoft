from fastapi import APIRouter, status, Response, HTTPException
from SchemaStudent import StudentPublic, StudentSchema, StudentsList
from ServiceStudent import first_letter_dont_repeat, Student_CRUD

router_student = APIRouter()

@router_student.get("/getStudents", response_model=StudentsList)
def getStudents(res: Response) -> list:
    """
    Endpoint para recuperar a lista de estudantes.

    Retorna:
        StudentsList: Uma lista de todos os estudantes no banco de dados.

    Respostas:
        200 OK: Retorna um objeto JSON contendo a lista de estudantes.
        404 Not Found: Se não existirem estudantes no banco de dados.
    """
    students = Student_CRUD.get_students()
    print(students)
    
    if students is None or not students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Students not found"
        )
    
    res.status_code = status.HTTP_200_OK
    
    return students

@router_student.post("/addNewStudent", response_model=StudentPublic)
def createStudent(newStudent: StudentSchema, res: Response) -> StudentPublic:
    """
    Adiciona um novo estudante ao banco de dados.
    Este endpoint recebe os dados de um estudante, calcula a primeira letra do nome que não se repete,
    cria um novo registro de estudante e o adiciona ao banco de dados em memória.
    Parâmetros:
    - student (StudentSchema): Objeto contendo os dados do estudante (nome e pontuação).
    Retorna:
    - StudentPublic: Dados do estudante criado, incluindo o ID, nome, pontuação e a primeira letra não repetida do nome.
    Respostas:
    - 201: Estudante criado com sucesso.
    """
    if not newStudent or newStudent is {}:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )
        
    firstLetter = first_letter_dont_repeat(newStudent.name)  
    
    student_data = newStudent.model_dump()
    student_data["firstLetter"] = firstLetter
    
    result = Student_CRUD.create_students(student_data)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    res.status_code = status.HTTP_201_CREATED
    
    return result

