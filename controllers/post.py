from typing import Annotated

from fastapi import Query, status, APIRouter

from schemas.post import PostRequest, UpdatePostRequest
from services.post import PostService
from views.post import PostResponse
from models.post import posts
from database import database

router = APIRouter(prefix="/posts")
service = PostService()


@router.get("/", response_model=list[PostResponse])
async def read_posts(
    published: Annotated[bool, Query(alias="published_at")],
    limit: int,
    skip: int = 0,
):
    query = (
        posts.select().where(posts.c.published == published).offset(skip).limit(limit)
    )
    return await database.fetch_all(query)


@router.get("/{id}", response_model=PostResponse)
async def read_post(id: int):
    return await service.read(id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(post: PostRequest):
    query = posts.insert().values(
        title=post.title,
        content=post.content,
        published_at=post.published_at,
        published=post.published,
    )
    last_id = await database.execute(query)
    return {**post.model_dump(), "id": last_id}


@router.patch("/{id}", response_model=PostResponse)
async def update_post(id: int, post: UpdatePostRequest):
    return await service.update(id=id, post=post)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete(id: int):
    return await service.delete(id)
