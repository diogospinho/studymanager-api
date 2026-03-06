Sobre o projeto

Esse projeto foi feito como atividade prática para desenvolver uma API RESTful de gerenciamento de usuários, cursos e matrículas.

A aplicação permite:

cadastro de usuários

cadastro de cursos

matrícula de usuários em cursos

consulta de dados

atualização e exclusão de registros

Para o desenvolvimento, utilizei FastAPI com SQLAlchemy, aplicando separação em camadas, uso de ORM, validações e tratamento de erros.

Objetivo

O objetivo da atividade era construir uma API organizada e funcional, aplicando conceitos de Arquitetura Limpa e Clean Code.

Além disso, o projeto precisava ter:

CRUD de usuários

CRUD de cursos

criação de matrículas

consulta relacional

validações de negócio

respostas padronizadas em JSON

Tecnologias utilizadas

Python

FastAPI

SQLAlchemy

SQLite

Pydantic

Uvicorn

Estrutura do projeto

O projeto foi dividido em camadas para separar melhor cada responsabilidade.

app/
├── api/
│   └── routes/
├── core/
├── entities/
├── infrastructure/
├── repositories/
├── schemas/
├── services/
└── main.py
Organização das camadas

routes: recebe as requisições HTTP

services: concentra as regras de negócio

repositories: faz o acesso ao banco

entities: define os modelos ORM

infrastructure: contém a configuração do banco

schemas: define validação e serialização dos dados

core: centraliza configurações e tratamento de erros

Essa organização ajuda a deixar o código mais limpo, mais fácil de entender e mais simples de manter.

Modelagem do banco
User

id

name

email (único)

created_at

Course

id

title

description

workload

Enrollment

id

user_id

course_id

enrolled_at

Relacionamentos

um usuário pode ter várias matrículas

um curso pode ter várias matrículas

uma matrícula pertence a um usuário e a um curso

Funcionalidades implementadas
Usuários

POST /users

GET /users

GET /users/{id}

PUT /users/{id}

DELETE /users/{id}

Cursos

POST /courses

GET /courses

GET /courses/{id}

PUT /courses/{id}

DELETE /courses/{id}

Matrículas

POST /enrollments

Consulta relacional

GET /users/{id}/courses

Esse endpoint retorna os dados do usuário e os cursos em que ele está matriculado.

Regras aplicadas

Durante a implementação, foram definidas algumas regras:

o email do usuário deve ser único

os campos obrigatórios precisam ser validados

não pode existir matrícula duplicada

só é possível matricular se o usuário existir

só é possível matricular se o curso existir

quando um registro não é encontrado, a API retorna erro padronizado

Padrão de resposta

As respostas da API seguem um formato JSON padronizado.

Exemplo de sucesso
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 1,
    "name": "João Silva",
    "email": "joao@email.com"
  }
}
Exemplo de erro
{
  "success": false,
  "message": "User not found",
  "data": null
}

Também foram usados códigos HTTP adequados em cada situação.

Como executar o projeto
1. Clonar o repositório
git clone https://github.com/SEU_USUARIO/studymanager-api.git
2. Entrar na pasta do projeto
cd studymanager-api
3. Criar o ambiente virtual
python -m venv .venv
4. Ativar o ambiente virtual

No Windows:

.venv\Scripts\Activate

No Linux/Mac:

source .venv/bin/activate
5. Instalar as dependências
pip install -r requirements.txt
6. Criar o arquivo .env

Criar o arquivo .env com base no .env.example.

7. Rodar a aplicação
uvicorn app.main:app --reload
8. Acessar a documentação
http://127.0.0.1:8000/docs
Testes realizados

Os testes foram feitos manualmente pelo Swagger.

Testes de usuários

cadastro

listagem

busca por ID

atualização

exclusão

Testes de cursos

cadastro

listagem

busca por ID

atualização

exclusão

Testes de matrículas

criação de matrícula

consulta dos cursos de um usuário

Testes de erro

tentativa de cadastro com email duplicado

tentativa de matrícula duplicada

busca de usuário inexistente

matrícula com usuário inexistente

matrícula com curso inexistente

Clean Code e organização

Procurei manter o código com nomes claros, métodos mais curtos e responsabilidades separadas. A lógica de negócio ficou fora das rotas, o acesso ao banco ficou concentrado nos repositories e o tratamento de erro foi padronizado para evitar respostas inconsistentes.
