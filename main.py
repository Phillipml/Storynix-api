from fastapi import FastAPI
import sqlalchemy as sa
from controllers import post
import databases
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite:///./blog.db"
database = databases.Database(DATABASE_URL)

metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
