from datetime import datetime
from pydantic import BaseModel


class PostResponse(BaseModel):
    title: str
    date: datetime
    published_at: bool
