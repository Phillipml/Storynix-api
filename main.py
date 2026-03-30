from datetime import UTC,datetime
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {'title':"Criando aplicação com Django",'date':datetime.now(UTC), 'published': True},
    {'title':"Internacionalizando uma app FastApi",'date':datetime.now(UTC), 'published': True},
    {'title':"Criando aplicação com Flask",'date':datetime.now(UTC), 'published': False},
    {'title':"Internacionalizando uma app Starlett",'date':datetime.now(UTC), 'published': True},
]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False

@app.post('/post/', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post

@app.get("/posts/")
def read_posts(published: bool, limit: int, skip: int = 0):
    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post["published"] is published:
            posts.append(post)
    return posts
    
@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {'posts':[
    {'title':f"Criando aplicação com {framework}",'date':datetime.now(UTC)},
    {'title':f"Internacionalizando uma app {framework}",'date':datetime.now(UTC)},
]}

