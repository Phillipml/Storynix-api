from datetime import datetime, UTC
from pydantic import BaseModel


class PostRequest(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published_at: bool = False
