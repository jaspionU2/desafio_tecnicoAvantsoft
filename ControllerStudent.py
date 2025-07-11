from fastapi import APIRouter, status, Response, HTTPException
from SchemaStudent import StudentPublic, StudentSchema, StudentsList, first_letter_dont_repeat
from ServiceStudent import Student_CRUD

router_student = APIRouter()

@router_student.get("/getStudents", response_model=StudentsList)
def getStudents(res: Response):
    """
    Endpoint para recuperar a lista de estudantes.

    Retorna:
        StudentsList: Uma lista de todos os estudantes no banco de dados.

    Respostas:
        200 OK: Retorna um objeto JSON contendo a lista de estudantes.
        404 Not Found: Se não existirem estudantes no banco de dados.
    """
    students = Student_CRUD.get_students()
    
    if students is None or students is []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    res.status_code = status.HTTP_200_OK
    
    return students

@router_student.post("/addNewStudent", response_model=StudentPublic)
def createStudent(student: StudentSchema, res: Response) -> StudentPublic:
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
    if not student or student is {}:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT
        )
    
    
    result = Student_CRUD.create_students(student.model_dump())
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    
    res.status_code = status.HTTP_201_CREATED
    
    return result

# @router_student.put("/updateStudent/{id}", response_model=StudentPublic, status_code=status.HTTP_202_ACCEPTED)
# def updateStudent(id: int, student: StudentSchema):
#     """
#     Atualiza as informações de um estudante existente no banco de dados.
#     Parâmetros:
#     - id (int): O identificador único do estudante a ser atualizado.
#     - student (StudentSchema): Objeto contendo os novos dados do estudante.
#     Retorna:
#     - StudentPublic: Os dados atualizados do estudante.
#     Códigos de status:
#     - 202 ACCEPTED: Atualização realizada com sucesso.
#     - 404 NOT FOUND: Estudante não encontrado.
#     - 204 NO CONTENT: Nenhuma informação foi fornecida para atualização.
#     Detalhes:
#     - Verifica se o ID fornecido é válido e corresponde a um estudante existente.
#     - Gera a primeira letra não repetida do nome do estudante.
#     - Atualiza os dados do estudante no banco de dados (DataBase).
#     """
    
#     if id <= 0 or id > len(DataBase):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Student not found"
#         )
         
#     if not student or student is []:
#         raise HTTPException(
#             status_code=status.HTTP_204_NO_CONTENT,
#             detail="No information has been added"
#             )
    
#     nonRepeatedLetter = first_letter_dont_repeat(student.name)

#     Student = StudentPublic(
#         id=id,
#         name=student.name,
#         score=student.score,
#         nonRepeatedLetter=nonRepeatedLetter
#     )
    
#     DataBase[id - 1] = Student
    
#     return Student

# @router_student.delete("/deleteStudent/{id}", status_code=status.HTTP_200_OK)
# def deleteStudent(id: int):
#     """
#     Deleta um estudante do banco de dados pelo seu ID.
#     Parâmetros:
#     - id (int): O ID do estudante a ser deletado.
#     Retorno:
#     - status HTTP 200 OK em caso de sucesso.
#     - status HTTP 404 NOT FOUND se o estudante não for encontrado.
#     Exceções:
#     - HTTPException: Lançada se o ID for inválido ou se o estudante não existir.
#     Exemplo de uso:
#     DELETE /deleteStudent/1
#     """
#     if id <= 0 or id > len(DataBase):
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Student not found"
#         )
        
#     del DataBase[id - 1]
    
