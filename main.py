from datetime import UTC,datetime
from fastapi import FastAPI

app = FastAPI()

fake_db = [
    {'title':"Criando aplicação com Django",'date':datetime.now(UTC), 'published': True},
    {'title':"Internacionalizando uma app FastApi",'date':datetime.now(UTC), 'published': True},
    {'title':"Criando aplicação com Flask",'date':datetime.now(UTC), 'published': False},
    {'title':"Internacionalizando uma app Starlett",'date':datetime.now(UTC), 'published': True},
]

@app.get("/posts")
def read_posts(published: bool = True, skip: int = 0, limit: int = len(fake_db)):
    return [
        post
        for post in fake_db[skip : skip + limit]
        if post["published"] == published
    ]

@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {'posts':[
    {'title':f"Criando aplicação com {framework}",'date':datetime.now(UTC)},
    {'title':f"Internacionalizando uma app {framework}",'date':datetime.now(UTC)},
]}