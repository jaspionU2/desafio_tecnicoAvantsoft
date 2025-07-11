# desafio_tecnicoAvantsoft

Objetivo: Avaliar lógica básica, sintaxe, estrutura simples de dados
Crie uma API simples com as rotas:
POST /students: cadastra um estudante com nome e nota (0 a 10)
GET /students: retorna uma lista com os estudantes cadastrados (exibindo id, nome e nota)
GET /students/:id: retorna os dados de um estudante específico pelo id (id, nome, nota)
Requisitos:
O armazenamento pode ser feito em memória (array, lista) ou em banco de dados, conforme a preferência do candidato
Deve validar se a nota está entre 0 e 10
Deve funcionar com pelo menos 3 registros diferentes
Para toda rota GET, adicionar um campo que retorna a primeira letra do nome que não se repete. Se todas as letras se repetirem, retornar '_'.
Exemplo: Se houver um estudante chamado "Gabriel", a letra não repetida do nome é 'g'. Se houver um estudante chamado "Anna", todas as letras se repetem, então o valor retornado deve ser '_'.**
