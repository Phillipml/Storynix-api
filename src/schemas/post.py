from datetime import datetime
from pydantic import BaseModel


class PostRequest(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False


class UpdatePostRequest(BaseModel):
    title: str | None = None
    content: str | None = None
    published_at: datetime | None = None
    published: bool | None = None
