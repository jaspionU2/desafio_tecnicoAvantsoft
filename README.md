# desafio_tecnicoAvantsoft

## Objetivo

Avaliar lógica básica, sintaxe e estrutura simples de dados.

## Desafio

Crie uma API simples com as seguintes rotas:

- **POST `/students`**  
    Cadastra um estudante com nome e nota (0 a 10).

- **GET `/students`**  
    Retorna uma lista com os estudantes cadastrados (exibindo id, nome e nota).

- **GET `/students/:id`**  
    Retorna os dados de um estudante específico pelo id (id, nome, nota).

## Requisitos

- O armazenamento pode ser feito em memória (array, lista) ou em banco de dados, conforme a preferência do candidato.
- Deve validar se a nota está entre 0 e 10.
- Deve funcionar com pelo menos **3 registros diferentes**.
- Para toda rota GET, adicionar um campo que retorna a **primeira letra do nome que não se repete**.  
    Se todas as letras se repetirem, retornar `_`.

    **Exemplo:**  
    - Estudante chamado "Gabriel": a letra não repetida do nome é `g`.  
    - Estudante chamado "Anna": todas as letras se repetem, então o valor retornado deve ser `_`.


## Como rodar a API

1. **Crie um ambiente virtual Python (opcional, mas recomendado):**
    ```bash
    python -m venv .venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

2. **Instale as dependências necessárias:**
    ```bash
    pip install fastapi pydantic sqlmodel
    ```

    > Caso ocorra algum erro indicando que alguma dependência não foi reconhecida, instale manualmente utilizando os comandos acima.

3. **Execute a aplicação:**
    ```bash
    fastapi run app.py
    ```
    ou
    ```bash
   fastaí dev app.py
    ```

4. **Acesse a documentação interativa (Swagger):**
    - Abra o navegador e acesse: [http://localhost/docs](http://localhost/docs)
    - Por meio dessa interface, é possível testar todas as rotas da API.