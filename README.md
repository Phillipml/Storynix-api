# Storynix

Projeto backend em Python usando FastAPI.

## Requisitos

- Python 3.13+
- Poetry 2+

## Tecnologias

- FastAPI
- Uvicorn

## Como rodar localmente

1. Instale as dependencias:

```bash
poetry install
```

2. Ative o ambiente virtual do Poetry:

```bash
poetry shell
```

3. Inicie a aplicacao:

```bash
uvicorn app.main:app --reload
```

Se preferir, rode sem entrar no shell:

```bash
poetry run uvicorn app.main:app --reload
```

## Estrutura esperada

Como o comando de execucao usa `app.main:app`, espera-se a seguinte estrutura:

```text
app/
  main.py
```

E no `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()
```

## Proximos passos sugeridos

- Definir uma descricao no `pyproject.toml` (`project.description`)
- Criar endpoints iniciais no `app/main.py`
- Adicionar testes automatizados
