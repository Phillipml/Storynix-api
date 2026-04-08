# Storynix

API backend em Python com FastAPI para gerenciamento de posts e autenticação JWT.

## Stack

- Python 3.13+
- FastAPI
- Uvicorn
- SQLAlchemy Core
- Databases
- Pydantic
- PyJWT
- Ruff

## Requisitos

- Python 3.13+
- Poetry 2+

## Como executar localmente

1. Instale as dependencias:

```bash
poetry install
```

2. Suba a API com recarregamento automatico:

```bash
poetry run uvicorn main:app --reload
```

3. Acesse:

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Banco de dados

- Banco local SQLite em `blog.db`.
- A conexao e criada em `database.py`.
- As tabelas sao criadas no startup da aplicacao (`lifespan` em `main.py`).

## Autenticação

- Login em `POST /auth/login` com JSON `{"user_id": <inteiro>}`.
- A resposta inclui `access_token` (string JWT).
- Todas as rotas em `/posts` exigem header `Authorization: Bearer <access_token>`.
- No Postman: **Authorization → Bearer Token** e cole apenas o valor do token (sem aspas). Corpo do login em **Body → raw → JSON** com `Content-Type: application/json`.
- Tokens antigos emitidos com `sub` numerico podem ser rejeitados pelo PyJWT 2.10+; em caso de duvida, faça login novamente para obter um token novo.

A logica de assinatura e validacao esta em `security.py`.

## Estrutura do projeto

```text
Storynix/
  main.py
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

- `GET /posts/` — lista posts com paginacao
  - query params: `published_at` (boolean), `limit` (int), `skip` (int opcional, default `0`)
- `GET /posts/{id}` — retorna um post por id
- `POST /posts/` — cria um post
- `PATCH /posts/{id}` — atualiza campos parcialmente
- `DELETE /posts/{id}` — remove um post

## Payloads

### Login (`POST /auth/login`)

```json
{
  "user_id": 1
}
```

### Criacao (`POST /posts/`)

```json
{
  "title": "Meu post",
  "content": "Conteudo do post",
  "published_at": "2024-03-21T10:20:00+03:00",
  "published": true
}
```

### Atualizacao parcial (`PATCH /posts/{id}`)

```json
{
  "published_at": "2024-03-21T10:20:00+03:00",
  "published": true
}
```

Observacoes:

- Use a chave `published_at` (com underscore). Chaves como `"published at"` nao atualizam o campo.
- A rota correta usa id numerico sem `:`. Exemplo: `PATCH /posts/1`.

## Modelos

- `LoginRequest` / `LoginResponse` (`schemas/auth.py`, `views/auth.py`)
- `PostRequest` (`schemas/post.py`): payload de entrada para criacao
- `UpdatePostRequest` (`schemas/post.py`): payload de entrada para atualizacao parcial
- `PostResponse` (`views/post.py`): payload de saida

## Qualidade de codigo

Rodar lint com Ruff:

```bash
poetry run ruff check .
```
