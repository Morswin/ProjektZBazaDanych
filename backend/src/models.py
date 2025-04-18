from datetime import date, time, datetime
from enum import Enum
from sqlmodel import Field, SQLModel

class TicketType(Enum):
    COMPLAIN = 1
    FOOD_NOT_DELIVERED = 2
    FOOD_IS_COLD = 3

class TicketState(Enum):
    PENDING = 1
    RESOLVED = 2
    REJECTED = 3

class Ticket(SQLModel, table=True):
    id_ticket: int | None = Field(default=None, primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id_user")
    ticket_type: TicketType
    ticket_state: TicketState
    description: str

class UserType(Enum):
    GUEST = 1
    USER = 2
    ADMINISTRATOR = 3
    DRIVER = 4

class Gender(Enum):
    FEMALE = 1
    MALE = 2
    OTHER = 3
    UNSPECIFIED = 3

class User(SQLModel, table=True):
    id_user: int | None = Field(default=None, primary_key=True)
    user_type: UserType
    name: str
    surename: str
    phone: str
    email: str
    gender: Gender
    pay: float

class OrderStatus(Enum):
    SUBMITED = 1
    COOKING = 2
    REDY_AT_RESTAURANT = 3
    IN_DELIVERY = 4
    DELIVERED = 5
    CANCELLED = 6

class Order(SQLModel, table=True):
    id_order: int | None = Field(default=None, primary_key=True)
    id_address: int | None = Field(default=None, foreign_key="address.id_address")
    id_restaurant: int | None = Field(default=None, foreign_key="restaurant.id_restaurant")
    id_ticket: int | None = Field(default=None, foreign_key="ticket.id_ticket")
    status: OrderStatus
    price: float
    order_date: datetime
    weight: float
    score_driver: float
    score_restaurant: float

class Address(SQLModel, table=True):
    id_address: int | None = Field(default=None, primary_key=True)
    city: str
    street: str
    zip_code: str
    house_number: int
    apartment_number: int

class Food(SQLModel, table=True):
    id_food: int | None = Field(default=None, primary_key=True)
    id_restaurant: int | None = Field(default=None, foreign_key="restaurant.id_restaurant")
    name: str
    description: str
    # alergens: str  # For now we will not implement this. It may be a separate table with a many to many relation.
    price: float

class Restaurant(SQLModel, table=True):
    id_restaurant: int | None = Field(default=None, primary_key=True)
    id_hours: int | None = Field(default=None, foreign_key="hours.id_hours")
    id_score: int | None = Field(default=None, foreign_key="score.id_score")
    name: str
    pay_cut: float
    email: str
    phone: str

class Driver(SQLModel, table=True):
    id_driver: int | None = Field(default=None, primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id_user")
    id_hours: int | None = Field(default=None, foreign_key="hours.id_hours")
    id_vehicle: int | None = Field(default=None, foreign_key="vehicle.id_vehicle")
    id_score: int | None = Field(default=None, foreign_key="score.id_score")
    date_drivers_license: date
    date_ID: date
    is_occupied: bool

class Vehicle(SQLModel, table=True):
    id_vehicle: int | None = Field(default=None, primary_key=True)
    id_vehicle_type: int | None = Field(default=None, foreign_key="vehicletype.id_vehicle_type")
    brand: str
    model: str

class Vehicletype(SQLModel, table=True):
    id_vehicle_type: int | None = Field(default=None, primary_key=True)
    name: str
    max_weight: float  # How much it can carry in it's cargo or such

class Hours(SQLModel, table=True):
    id_hours: int | None = Field(default=None, primary_key=True)
    day: str  # Let's rediscuss if Varchar makes sense here, but for now it stays
    time_from: time
    time_t: time

class Score(SQLModel, table=True):
    id_score: int | None = Field(default=None, primary_key=True)
    amount: int
    sum: float
