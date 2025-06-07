from models import Restaurant, User, UserCreate, UserType, Gender, Food, OrderCreate, Order, OrderStatus, FoodOrder
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


@app.get("/restaurant", response_model=Restaurant)
def restaurant_info(restaurant_id: int, session: Session = Depends(get_session)):
    restaurant = session.exec(select(Restaurant).where(Restaurant.id == restaurant_id)).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@app.get("/availablefood", response_model=list[Food])
def available_food_in_restaurant(restaurant_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Food).where(Food.restaurant_id == restaurant_id)).all()


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

# class OrderCreate(SQLModel):
#     food_id: list[int]
#     price: int
#     user: int
#     restaurant: int

# class Order(SQLModel, table=True):
#     __tablename__ = "order"

#     # Keys
#     id: int | None = Field(default=None, primary_key=True)
#     address_id: int | None = Field(default=None, foreign_key="address.id")
#     restaurant_id: int | None = Field(default=None, foreign_key="restaurant.id")
#     ticket_id: int | None = Field(default=None, foreign_key="ticket.id")

#     # Relations
#     users: list["OrderHistory"] = Relationship(back_populates="order")
#     food_orders: list["FoodOrder"] = Relationship(back_populates="order")
#     address: Address | None = Relationship(back_populates="orders")
#     restaurant: Restaurant | None = Relationship(back_populates="orders")
#     tickets: Ticket | None = Relationship(back_populates="orders")

#     # Fields
#     status: OrderStatus
#     price: float
#     order_date: datetime | None
#     weight: float | None
#     score_driver: float | None
#     score_restaurant: float | None

@app.post("/order", response_model=Order)
def create_order(order_data: OrderCreate, session: Session = Depends(get_session)):
    new_order = Order(
        status = OrderStatus.SUBMITED,
        price = order_data.price,
        # food_orders = [],
        restaurant = session.exec(select(Restaurant).where(Restaurant.id == order_data.restaurant_id)).first()
    )
    session.add(new_order)
    food_order = []
    for f in order_data.food_id:
        n_f = FoodOrder(
            order = new_order,
            food = session.exec(select(Food).where(Food.id == f)).first()
        )
        session.add(n_f)
        food_order.append(n_f)
    # new_order.food_orders = food_order
    # user = session.exec(select(User).where(User.id == order_data.user_id)).first()
    # user.
    session.commit()
    session.refresh(new_order)
    return new_order
