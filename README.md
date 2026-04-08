# Storynix

API em Python com FastAPI: posts (SQLite) e autenticação JWT. O código da aplicação vive no pacote **`src`**; os imports são absolutos (`from src....`).

## Stack

- Python 3.13+
- FastAPI, Uvicorn
- SQLAlchemy Core, Databases (aiosqlite)
- Pydantic, Pydantic Settings
- PyJWT, Ruff, Pytest + HTTPX (integração)

## Requisitos

- Python 3.13+
- Poetry 2+

## Configuração

1. Na raiz do repositório, copie o exemplo de ambiente:

```bash
cp .env.example .env
```

No Windows (cmd/PowerShell): `copy .env.example .env`

2. Variáveis relevantes:

| Variável        | Descrição |
|----------------|-----------|
| `DATABASE_URL` | URL do banco. Padrão no código: `sqlite:///./blog.db` se ausente. |
| `ENVIRONMENT`  | `local` (ou qualquer valor ≠ `production`): SQLite com `check_same_thread=False`. `production`: engine sem esse argumento. |

O `Settings` (`src/config.py`) lê `.env` na **raiz do projeto** e em **`src/`**, na ordem (arquivos inexistentes são ignorados).

## Executar localmente

```bash
poetry install
poetry run uvicorn src.main:app --reload
```

Execute sempre a partir da **raiz** do repositório (o Python precisa resolver o pacote `src`).

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

O SQLite padrão (`sqlite:///./blog.db`) cria `blog.db` no **diretório de trabalho atual** (normalmente a raiz do repo).

## Deploy (ex.: Render)

- **Start Command:** `poetry run uvicorn src.main:app --host 0.0.0.0 --port $PORT`  
  (`$PORT` é variável do Render; em PowerShell local use por exemplo `$env:PORT = 8000` ou passe `--port 8000`.)
- **Build:** `poetry install --no-interaction --no-ansi` (ou equivalente da sua imagem).
- Defina **`DATABASE_URL`** (em produção costuma ser Postgres; SQLite em disco efêmero some entre deploys).
- Defina **`ENVIRONMENT=production`** se quiser o perfil “production” do `database.py`.

Não é necessário `PYTHONPATH=src` se o diretório de trabalho for a raiz do repositório.

## Banco de dados

- Conexão e metadata: `src/database.py`.
- Tabelas criadas no startup: `lifespan` em `src/main.py`.

## Testes

Na raiz:

```bash
poetry run pytest
```

Opções úteis: `pytest -q`, `pytest tests/integration/controllers/auth/ -v`.

O `tests/conftest.py` define `DATABASE_URL=sqlite:///tests.db` antes de importar a app; pode surgir `tests.db` na raiz ao rodar os testes (ideal manter fora do Git; o `.gitignore` já cobre `*.db` na raiz).

## Autenticação

- `POST /auth/login` com `{"user_id": <int>}` → resposta com `access_token` (JWT).
- Rotas `/posts/*` exigem `Authorization: Bearer <token>`.
- Postman: **Bearer Token** só com o JWT; login em **Body → raw → JSON**.
- Claim `sub` como string (PyJWT 2.10+). JWT em `src/security.py`.

## Estrutura

```text
Storynix/
  pyproject.toml
  .env.example
  tests/
    conftest.py
    integration/controllers/auth|post/
  src/
    __init__.py
    main.py
    config.py
    database.py
    security.py
    exceptions.py
    controllers/   # pacote ( __init__.py )
    services/
    models/
    schemas/
    views/
```

## Endpoints

### Auth — `/auth`

- `POST /auth/login` → JWT (`access_token`)

### Posts — `/posts` (Bearer obrigatório)

- `GET /posts/?published_at=<bool>&limit=<int>&skip=<int>` — listagem
- `GET /posts/{id}`
- `POST /posts/`
- `PATCH /posts/{id}`
- `DELETE /posts/{id}`

## Payloads

**Login**

```json
{ "user_id": 1 }
```

**Criar post**

```json
{
  "title": "Meu post",
  "content": "Conteudo do post",
  "published_at": "2024-03-21T10:20:00+03:00",
  "published": true
}
```

**Atualizar post (parcial)**

```json
{
  "published_at": "2024-03-21T10:20:00+03:00",
  "published": true
}
```

Use a query `published_at` (boolean), não `published=on`. IDs na URL numéricos: `/posts/1`.

## Modelos Pydantic (`src/`)

- `LoginRequest` / `LoginResponse` — `schemas/auth.py`, `views/auth.py`
- `PostRequest`, `UpdatePostRequest` — `schemas/post.py`
- `PostResponse` — `views/post.py`

## Lint

```bash
poetry run ruff check .
```
