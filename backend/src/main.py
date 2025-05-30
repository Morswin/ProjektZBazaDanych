from models import Restaurant, User, UserCreate, UserType, Gender
from sqlmodel import SQLModel, create_engine, select, Session
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import populate


sqlite_file = "db.sqlite" 
sqlite_url = f"sqlite:///db/{sqlite_file}"
engine = create_engine(sqlite_url, echo=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    populate.populate(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # używaj konkretnego originu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/restaurants", response_model=list[Restaurant])
def list_restaurants(session: Session = Depends(get_session)):
    return session.exec(select(Restaurant)).all()


@app.get("/login", response_model=User)
def login(email: str, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/register", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    new_user = User(
        user_type = UserType.USER,
        name = user.name,
        surename = user.surename,
        phone = user.phone,
        email = user.email,
        gender = Gender.UNSPECIFIED,
        pay = 0
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user