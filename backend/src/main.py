from sqlmodel import SQLModel, create_engine
from contextlib import asynccontextmanager
from fastapi import FastAPI
import populate


# SQLModel
sqlite_file = "db.sqlite" 
sqlite_url = f"sqlite:///db/{sqlite_file}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize things
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)
    populate.populate(engine)
    yield
    # Deinitialize


# FastAPI
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}
