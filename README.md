# Storynix

API backend em Python com FastAPI para gerenciamento de posts.

## Stack

- Python 3.13+
- FastAPI
- Uvicorn
- SQLAlchemy Core
- Databases
- Pydantic
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

## Estrutura do projeto

```text
Storynix/
  main.py
  database.py
  controllers/
    post.py
  services/
    post.py
  models/
    post.py
  schemas/
    post.py
  views/
    post.py
```

## Endpoints

Base: `/posts`

- `GET /posts/` lista posts com paginacao
  - query params: `published_at` (boolean), `limit` (int), `skip` (int opcional, default `0`)
- `GET /posts/{id}` retorna um post por id
- `POST /posts/` cria um post
- `PATCH /posts/{id}` atualiza campos parcialmente
- `DELETE /posts/{id}` remove um post

## Payloads

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

Observacao importante:

- Use a chave `published_at` (com underscore). Chaves como `"published at"` nao atualizam o campo.
- A rota correta usa id numerico sem `:`. Exemplo: `PATCH /posts/1`.

## Modelos

- `PostRequest` (`schemas/post.py`): payload de entrada para criacao
- `UpdatePostRequest` (`schemas/post.py`): payload de entrada para atualizacao parcial
- `PostResponse` (`views/post.py`): payload de saida

## Qualidade de codigo

Rodar lint com Ruff:

```bash
poetry run ruff check .
```
