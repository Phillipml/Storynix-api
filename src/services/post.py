from databases.interfaces import Record
from fastapi import HTTPException, status
from src.database import database
from src.models.post import posts
from src.schemas.post import PostRequest, UpdatePostRequest


class PostService:
    async def count(self, id: int) -> int:
        query = "select count(id) as total from posts where id = :id"
        result = await database.fetch_one(query, {"id": id})
        return result.total

    async def __get_by_id(self, id) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post no found"
            )
        return post

    async def read_all(
        self, published: bool, limit: int, skip: int = 0
    ) -> list[Record]:
        query = posts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def create(self, post: PostRequest) -> int:
        query = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )
        return await database.execute(query)

    async def update(self, id: int, post: UpdatePostRequest) -> Record:
        total = await self.count(id)
        if not total:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
            )

        data = post.model_dump(exclude_unset=True)
        query = posts.update().where(posts.c.id == id).values(**data)
        await database.execute(query)

        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:
        query = posts.delete().where(posts.c.id == id)
        await database.execute(query)
