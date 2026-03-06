# StudyManager API

API RESTful para gerenciamento de usuários, cursos e matrículas, desenvolvida com **FastAPI + SQLAlchemy**, seguindo **Arquitetura Limpa**, **Clean Code** e uso de **ORM**.

## 1. Tecnologias
- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- SQLite
- Uvicorn

## 2. Estrutura de pastas
```bash
studymanager-api/
├── app/
│   ├── api/
│   │   ├── dependencies.py
│   │   └── routes/
│   │       ├── users.py
│   │       ├── courses.py
│   │       └── enrollments.py
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── response.py
│   ├── entities/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── course.py
│   │   └── enrollment.py
│   ├── infrastructure/
│   │   └── database.py
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── course_repository.py
│   │   └── enrollment_repository.py
│   ├── schemas/
│   │   ├── common.py
│   │   ├── user.py
│   │   ├── course.py
│   │   └── enrollment.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── course_service.py
│   │   └── enrollment_service.py
│   └── main.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## 3. Justificativa da organização
A aplicação foi organizada em camadas para isolar responsabilidades e facilitar manutenção, testes e evolução. As **routes/controllers** recebem a requisição HTTP e delegam a execução para os **services/use cases**, onde ficam as regras de negócio. Os **repositories** concentram o acesso ao banco via SQLAlchemy, evitando acoplamento direto da regra de negócio com a persistência. As **entities/models** representam as tabelas e relacionamentos do domínio. Já a camada de **infrastructure** cuida da conexão com banco e detalhes técnicos. Essa separação segue os princípios de Arquitetura Limpa, mantendo o código mais legível, testável e escalável.

## 4. Modelagem do banco
### User
- id
- name
- email (único)
- created_at

### Course
- id
- title
- description
- workload

### Enrollment
- id
- user_id
- course_id
- enrolled_at

### Relacionamentos
- Um usuário pode ter várias matrículas
- Um curso pode ter várias matrículas
- Uma matrícula pertence a um usuário e a um curso
- Restrição de unicidade composta em `(user_id, course_id)` para impedir matrícula duplicada

## 5. Como executar
### 5.1 Criar ambiente virtual
```bash
python -m venv .venv
```

### 5.2 Ativar o ambiente
**Windows**
```bash
.venv\Scripts\activate
```

**Linux/Mac**
```bash
source .venv/bin/activate
```

### 5.3 Instalar dependências
```bash
pip install -r requirements.txt
```

### 5.4 Configurar variáveis de ambiente
Crie um arquivo `.env` baseado no `.env.example`.

### 5.5 Executar API
```bash
uvicorn app.main:app --reload
```

A documentação ficará disponível em:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 6. Endpoints obrigatórios
### Users
- `POST /users`
- `GET /users`
- `GET /users/{id}`
- `PUT /users/{id}`
- `DELETE /users/{id}`
- `GET /users/{id}/courses`

### Courses
- `POST /courses`
- `GET /courses`
- `GET /courses/{id}`
- `PUT /courses/{id}`
- `DELETE /courses/{id}`

### Enrollments
- `POST /enrollments`

## 7. Exemplos de payloads
### Criar usuário
```json
{
  "name": "Diogo Silva",
  "email": "diogo@email.com"
}
```

### Criar curso
```json
{
  "title": "Python para APIs",
  "description": "Curso introdutório de FastAPI e SQLAlchemy",
  "workload": 20
}
```

### Criar matrícula
```json
{
  "user_id": 1,
  "course_id": 1
}
```

## 8. Exemplo de resposta padronizada
### Sucesso
```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": 1,
    "name": "Diogo Silva",
    "email": "diogo@email.com",
    "created_at": "2026-03-05T18:00:00"
  }
}
```

### Erro
```json
{
  "success": false,
  "message": "User not found",
  "data": null
}
```

## 9. Regras de negócio implementadas
- Email de usuário único
- Validação automática com Pydantic
- Matrícula duplicada bloqueada
- Verificação de existência de usuário e curso antes da matrícula
- Tratamento centralizado de exceções
- Retornos HTTP coerentes (`201`, `200`, `404`, `409`, `422`)

## 10. Passo a passo para subir no GitHub
```bash
git init
git add .
git commit -m "feat: initial StudyManager API"
git branch -M main
git remote add origin SEU_LINK_DO_GITHUB
git push -u origin main
```

## 11. Sugestão de apresentação da atividade
1. Explique rapidamente o domínio: usuários, cursos e matrículas.
2. Mostre a estrutura em camadas.
3. Aponte onde está cada responsabilidade.
4. Abra o Swagger e execute os endpoints.
5. Demonstre erro de email duplicado.
6. Demonstre erro de matrícula duplicada.
7. Mostre o endpoint relacional `/users/{id}/courses`.

## 12. Melhorias opcionais
- Dockerfile
- Testes automatizados com Pytest
- Alembic para migrations
- Paginação
- Soft delete
- Autenticação JWT
