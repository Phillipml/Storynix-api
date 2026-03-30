# Storynix

API backend em Python com FastAPI para gerenciamento de posts.

## Stack

- Python 3.13+
- FastAPI
- Uvicorn
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

## Estrutura do projeto

```text
Storynix/
  main.py
  controllers/
    post.py
  schemas/
    post.py
  views/
    post.py
```

## Endpoints atuais

Base: `/posts`

- `POST /posts/` cria um post
- `GET /posts/` lista posts com filtros e paginacao
- `GET /posts/{framework}` retorna posts por framework

## Modelos

- `PostRequest` (`schemas/post.py`): payload de entrada
- `PostResponse` (`views/post.py`): payload de saida

## Qualidade de codigo

Rodar lint com Ruff:

```bash
poetry run ruff check .
```

## Observacoes

- Os dados estao em memoria (`fake_db`) para fins de estudo/desenvolvimento.
- Campo `project.description` em `pyproject.toml` ainda esta vazio e pode ser preenchido.
