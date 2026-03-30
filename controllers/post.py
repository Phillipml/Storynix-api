from datetime import UTC, datetime
from typing import Annotated
from fastapi import Response, Cookie, Header, status, APIRouter

from schemas.post import PostRequest
from views.post import PostResponse


router = APIRouter(prefix="/posts")
fake_db = [
    {
        "title": "Criando aplicação com Django",
        "date": datetime.now(UTC),
        "published_at": True,
    },
    {
        "title": "Internacionalizando uma app FastApi",
        "date": datetime.now(UTC),
        "published_at": True,
    },
    {
        "title": "Criando aplicação com Flask",
        "date": datetime.now(UTC),
        "published_at": False,
    },
    {
        "title": "Internacionalizando uma app Starlett",
        "date": datetime.now(UTC),
        "published_at": True,
    },
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostRequest):
    fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostResponse])
def read_posts(
    response: Response,
    published_at: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="user", value="user@user.com")
    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")
    tail = skip + limit
    return [post for post in fake_db[skip:tail] if post["published_at"] is published_at]


@router.get("/{framework}", response_model=PostResponse)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {
                "title": f"Criando aplicação com {framework}",
                "published_at": datetime.now(UTC),
            },
            {
                "title": f"Internacionalizando uma app {framework}",
                "published_at": datetime.now(UTC),
            },
        ]
    }
