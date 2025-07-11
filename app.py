from fastapi import FastAPI, status, HTTPException
from SchemaStudent import StudentPublic, StudentSchema, StudentsList, first_letter_dont_repeat

app = FastAPI()

DataBase = []

@app.get("/getStudents", response_model=StudentsList, status_code=status.HTTP_200_OK)
def getStudents():
    """
    Endpoint para recuperar a lista de estudantes.

    Retorna:
        StudentsList: Uma lista de todos os estudantes no banco de dados.

    Lança:
        HTTPException: Se não houver estudantes no banco de dados, retorna status 404 com uma mensagem de detalhe.

    Respostas:
        200 OK: Retorna um objeto JSON contendo a lista de estudantes.
        404 Not Found: Se não existirem estudantes no banco de dados.
    """
    if not DataBase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dont exist students"
        )

    return {'students': DataBase}

@app.post("/addNewStudent", response_model=StudentPublic, status_code=status.HTTP_201_CREATED)
def createStudent(student: StudentSchema) -> StudentPublic:
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
    nonRepeatedLetter = first_letter_dont_repeat(student.name)

    newStudent = StudentPublic(
        id=len(DataBase) + 1,
        name=student.name,
        score=student.score,
        nonRepeatedLetter=nonRepeatedLetter
    )

    DataBase.append(newStudent)
    
    return newStudent

@app.put("/updateStudent/{id}", response_model=StudentPublic, status_code=status.HTTP_202_ACCEPTED)
def updateStudent(id: int, student: StudentSchema):
    """
    Atualiza as informações de um estudante existente no banco de dados.
    Parâmetros:
    - id (int): O identificador único do estudante a ser atualizado.
    - student (StudentSchema): Objeto contendo os novos dados do estudante.
    Retorna:
    - StudentPublic: Os dados atualizados do estudante.
    Códigos de status:
    - 202 ACCEPTED: Atualização realizada com sucesso.
    - 404 NOT FOUND: Estudante não encontrado.
    - 204 NO CONTENT: Nenhuma informação foi fornecida para atualização.
    Detalhes:
    - Verifica se o ID fornecido é válido e corresponde a um estudante existente.
    - Gera a primeira letra não repetida do nome do estudante.
    - Atualiza os dados do estudante no banco de dados (DataBase).
    """
    
    if id <= 0 or id > len(DataBase):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
         
    if not student or student is []:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="No information has been added"
            )
    
    nonRepeatedLetter = first_letter_dont_repeat(student.name)

    Student = StudentPublic(
        id=id,
        name=student.name,
        score=student.score,
        nonRepeatedLetter=nonRepeatedLetter
    )
    
    DataBase[id - 1] = Student
    
    return Student

@app.delete("/deleteStudent/{id}", status_code=status.HTTP_200_OK)
def deleteStudent(id: int):
    """
    Deleta um estudante do banco de dados pelo seu ID.
    Parâmetros:
    - id (int): O ID do estudante a ser deletado.
    Retorno:
    - status HTTP 200 OK em caso de sucesso.
    - status HTTP 404 NOT FOUND se o estudante não for encontrado.
    Exceções:
    - HTTPException: Lançada se o ID for inválido ou se o estudante não existir.
    Exemplo de uso:
    DELETE /deleteStudent/1
    """
    if id <= 0 or id > len(DataBase):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
        
    del DataBase[id - 1]
    

"""
Ponto de entrada principal da aplicação.

Quando o arquivo é executado diretamente, este bloco inicializa o servidor ASGI usando o Uvicorn,
expondo a aplicação FastAPI na máquina local (host 127.0.0.1) na porta 8080.

Exemplo de execução:
    python app.py

Após a execução, a API estará disponível em:
    http://127.0.0.1:8080

O Uvicorn é um servidor ASGI leve e rápido, recomendado para aplicações FastAPI.
"""
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
