from fastapi import Response, status, APIRouter

from schemas.post import PostRequest
from views.post import PostResponse


router = APIRouter(prefix="/posts")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostRequest):
    # fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostResponse])
def read_posts(
    response: Response,
    published_at: bool,
    limit: int,
    skip: int = 0,
):
    return []
