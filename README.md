# Storynix

API backend em Python com FastAPI para gerenciamento de posts e autenticação JWT.

## Stack

- Python 3.13+
- FastAPI
- Uvicorn
- SQLAlchemy Core
- Databases
- Pydantic / Pydantic Settings
- PyJWT
- Ruff
- Pytest (testes de integração)

## Requisitos

- Python 3.13+
- Poetry 2+

## Configuração

1. Copie o exemplo de variáveis de ambiente (na raiz do repositório):

```bash
cp .env.example .env
```

2. Ajuste `.env` se precisar. Variáveis usadas pela app:

- `DATABASE_URL` — URL do banco (padrão no código: `sqlite:///./blog.db` se não estiver definida).
- `ENVIRONMENT` — `local` usa `check_same_thread=False` no SQLite; `production` não.

O `Settings` em `src/config.py` carrega `.env` da **raiz do projeto** e de **`src/`** (o que existir). Assim você pode rodar o Uvicorn a partir de `src/` ou da raiz sem perder as variáveis.

## Como executar localmente

1. Instale as dependências:

```bash
poetry install
```

2. Entre em `src/` e suba a API (imports relativos ao pacote da app):

```bash
cd src
poetry run uvicorn main:app --reload
```

3. Acesse:

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

O arquivo SQLite `./blog.db` é criado no **diretório de trabalho atual** do processo (em geral `src/` se você subiu o servidor de lá).

## Banco de dados

- SQLite por padrão (`DATABASE_URL` tipo `sqlite:///./blog.db`).
- Conexão e metadata em `src/database.py`.
- Tabelas criadas no startup (`lifespan` em `src/main.py`).

## Testes

Na **raiz** do repositório:

```bash
poetry run pytest
```

O `pyproject.toml` define `pythonpath = ["src"]` para os testes encontrarem os módulos da app. O `tests/conftest.py` configura `DATABASE_URL` para um SQLite de teste.

## Autenticação

- Login: `POST /auth/login` com JSON `{"user_id": <inteiro>}`.
- Resposta com `access_token` (JWT).
- Rotas em `/posts` exigem `Authorization: Bearer <access_token>`.
- No Postman: **Authorization → Bearer Token** com só o JWT (sem aspas). Login: **Body → raw → JSON** e `Content-Type: application/json`.
- O claim `sub` do JWT é string (compatível com PyJWT 2.10+); faça login de novo se um token antigo falhar.

Lógica JWT em `src/security.py`.

## Estrutura do projeto

```text
Storynix/
  pyproject.toml
  .env.example
  tests/
    conftest.py
    integration/
      controllers/
        auth/
        post/
  src/
    main.py
    config.py
    database.py
    security.py
    controllers/
      auth.py
      post.py
    services/
      post.py
    models/
      post.py
    schemas/
      auth.py
      post.py
    views/
      auth.py
      post.py
```

## Endpoints

### Auth

Base: `/auth`

- `POST /auth/login` — retorna JWT (`access_token`)

### Posts (protegidas)

Base: `/posts` (requer `Authorization: Bearer ...`)

- `GET /posts/` — lista com paginação  
  - query: `published_at` (boolean), `limit` (int), `skip` (opcional, default `0`)
- `GET /posts/{id}` — um post por id
- `POST /posts/` — cria post
- `PATCH /posts/{id}` — atualização parcial
- `DELETE /posts/{id}` — remove post

## Payloads

### Login (`POST /auth/login`)

```json
{
  "user_id": 1
}
```

### Criação (`POST /posts/`)

```json
{
  "title": "Meu post",
  "content": "Conteudo do post",
  "published_at": "2024-03-21T10:20:00+03:00",
  "published": true
}
```

### Atualização parcial (`PATCH /posts/{id}`)

```json
{
  "published_at": "2024-03-21T10:20:00+03:00",
  "published": true
}
```

- Use `published_at` (underscore), não `"published at"`.
- Id numérico na URL, ex.: `PATCH /posts/1`.

## Modelos (em `src/`)

- `LoginRequest` / `LoginResponse` — `schemas/auth.py`, `views/auth.py`
- `PostRequest`, `UpdatePostRequest` — `schemas/post.py`
- `PostResponse` — `views/post.py`

## Qualidade de código

```bash
poetry run ruff check .
```
