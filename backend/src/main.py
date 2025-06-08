from models import Restaurant, User, UserCreate, UserType, Gender, Food, OrderCreate, Order, OrderStatus, FoodOrder, FoodCreate, Ticket, TicketCreate, TicketState, TicketType
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
    session.commit()
    session.refresh(new_order)
    return new_order


@app.post("/newfood", response_model=Food)
def add_new_food_to_a_restaurant(food_data: FoodCreate, session: Session = Depends(get_session)):
    new_food = Food(
        name = food_data.name,
        price = food_data.price,
        restaurant = session.exec(select(Restaurant).where(Restaurant.id == food_data.restaurant_id)).first()
    )
    session.add(new_food)
    session.commit()
    session.refresh(new_food)
    return new_food


@app.post("/ticket", response_model=Ticket)
def make_a_complaint(ticket_data: TicketCreate, session: Session = Depends(get_session)):
    new_ticket = Ticket(
        ticket_type = TicketType.COMPLAIN,
        ticket_state = TicketState.PENDING,
        description = ticket_data.description
    )
    session.add(new_ticket)
    session.commit()
    session.refresh(new_ticket)
    return new_ticket
