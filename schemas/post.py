from datetime import datetime, UTC
from pydantic import BaseModel


class PostRequest(BaseModel):
    title: str
    content: str
    published_at: datetime | None = None
    published: bool = False
