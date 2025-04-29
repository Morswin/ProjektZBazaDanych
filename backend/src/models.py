from datetime import date, time, datetime
from enum import Enum
from sqlalchemy import Column
from sqlalchemy.types import Enum as SqlEnum
from sqlmodel import Field, SQLModel, Relationship


# It must be declared befor user and order for some reason. Otherwise the IDE spams with errors.
class OrderHistory(SQLModel, table=True):
    __tablename__ = "order_history"

    # Keys
    id_order: int | None = Field(default=None, foreign_key="order.id", primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id", primary_key=True)


class AddressList(SQLModel, table=True):
    __tablename__ = "address_list"

    #keys
    id_user: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    id_address: int | None = Field(default=None, foreign_key="address.id", primary_key=True)


class UserType(Enum):
    GUEST = 1
    USER = 2
    ADMINISTRATOR = 3
    DRIVER = 4


class Gender(Enum):
    FEMALE = 1
    MALE = 2
    OTHER = 3
    UNSPECIFIED = 4


class User(SQLModel, table=True):
    __tablename__ = "user"

    # Keys
    id: int | None = Field(default=None, primary_key=True)

    # Relations
    orders: list["Order"] = Relationship(back_populates="users", link_model=OrderHistory)
    addresses: list["Address"] = Relationship(back_populates="users", link_model=AddressList)
    tickets: list["Ticket"] = Relationship(back_populates="user")
    drivers: list["Driver"] = Relationship(back_populates="user")

    # Fields
    user_type: UserType = Field(sa_column=Column(SqlEnum(UserType)))
    name: str
    surename: str
    phone: str
    email: str
    gender: Gender = Field(sa_column=Column(SqlEnum(Gender)))
    pay: float


class TicketType(Enum):
    COMPLAIN = 1
    FOOD_NOT_DELIVERED = 2
    FOOD_IS_COLD = 3


class TicketState(Enum):
    PENDING = 1
    RESOLVED = 2
    REJECTED = 3


class Ticket(SQLModel, table=True):
    __tablename__ = "ticket"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.id")

    # Relations
    user: User | None = Relationship(back_populates="tickets")
    orders: list["Order"] = Relationship(back_populates="tickets")

    # Fields
    ticket_type: TicketType
    ticket_state: TicketState
    description: str


class Address(SQLModel, table=True):
    __tablename__ = "address"

    # Keys
    id: int | None = Field(default=None, primary_key=True)

    # Relations
    users: list["User"] = Relationship(back_populates="addresses", link_model=AddressList)
    orders: list["Order"] = Relationship(back_populates="address")

    # Fields
    city: str
    street: str
    zip_code: str
    house_number: int
    apartment_number: int


class Hours(SQLModel, table=True):
    __tablename__ = "hours"

    # Keys
    id: int | None = Field(default=None, primary_key=True)

    # Relations
    restaurants: list["Restaurant"] = Relationship(back_populates="hours")
    drivers: list["Driver"] = Relationship(back_populates="hours")

    # Fields
    day: str  # Let's rediscuss if Varchar makes sense here, but for now it stays
    time_from: time
    time_t: time


class Score(SQLModel, table=True):
    __tablename__ = "score"

    # Keys
    id: int | None = Field(default=None, primary_key=True)

    # Relations
    restaurants: list["Restaurant"] = Relationship(back_populates="score")
    drivers: list["Driver"] = Relationship(back_populates="score")

    # Fields
    amount: int
    sum: float


class Restaurant(SQLModel, table=True):
    __tablename__ = "restaurant"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    hours_id: int | None = Field(default=None, foreign_key="hours.id")
    score_id: int | None = Field(default=None, foreign_key="score.id")

    # Relations
    orders: list["Order"] = Relationship(back_populates="restaurant")
    foods: list["Food"] = Relationship(back_populates="restaurant")
    hours: Hours | None = Relationship(back_populates="restaurants")
    score: Score | None = Relationship(back_populates="restaurants")

    # Fields
    name: str
    pay_cut: float
    email: str
    phone: str


class OrderStatus(Enum):
    SUBMITED = 1
    COOKING = 2
    REDY_AT_RESTAURANT = 3
    IN_DELIVERY = 4
    DELIVERED = 5
    CANCELLED = 6


class Order(SQLModel, table=True):
    __tablename__ = "order"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    address_id: int | None = Field(default=None, foreign_key="address.id")
    restaurant_id: int | None = Field(default=None, foreign_key="restaurant.id")
    ticket_id: int | None = Field(default=None, foreign_key="ticket.id")

    # Relations
    users: list["User"] = Relationship(back_populates="orders", link_model=OrderHistory)
    food_orders: list["FoodOrder"] = Relationship(back_populates="order")
    address: Address | None = Relationship(back_populates="orders")
    restaurant: Restaurant | None = Relationship(back_populates="orders")
    tickets: Ticket | None = Relationship(back_populates="orders")

    # Fields
    status: OrderStatus
    price: float
    order_date: datetime
    weight: float
    score_driver: float
    score_restaurant: float


class Food(SQLModel, table=True):
    __tablename__ = "food"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    restaurant_id: int | None = Field(default=None, foreign_key="restaurant.id")

    # Reltaions
    food_orders: list["FoodOrder"] = Relationship(back_populates="food")
    restaurant: Restaurant | None = Relationship(back_populates="foods")

    # Fields
    name: str
    description: str
    # alergens: str  # For now we will not implement this. It may be a separate table with a many to many relation.
    price: float


class FoodOrder(SQLModel, table=True):
    __tablename__ = "food_order"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    order_id: int | None = Field(default=None, foreign_key="order.id")
    food_id: int | None = Field(default=None, foreign_key="food.id")

    # Relations
    order: Order | None = Relationship(back_populates="food_orders")
    food: Food | None = Relationship(back_populates="food_orders")

    # Fields
    quantity: int


class VehicleType(SQLModel, table=True):
    __tablename__ = "vehicle_type"

    # Keys
    id: int | None = Field(default=None, primary_key=True)

    # Relations
    vehicles: list["Vehicle"] = Relationship(back_populates="vehicle_type")

    # Fields
    name: str
    max_weight: float  # How much it can carry in it's cargo or such


class Vehicle(SQLModel, table=True):
    __tablename__ = "vehicle"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    vehicle_type_id: int | None = Field(default=None, foreign_key="vehicle_type.id")

    # Relations
    drivers: list["Driver"] = Relationship(back_populates="vehicle")
    vehicle_type: VehicleType | None = Relationship(back_populates="vehicles")

    # Fields
    brand: str
    model: str


class Driver(SQLModel, table=True):
    __tablename__ = "driver"

    # Keys
    id: int | None = Field(default=None, primary_key=True)
    vehicle_id: int | None = Field(default=None, foreign_key="vehicle.id")
    hours_id: int | None = Field(default=None, foreign_key="hours.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")
    score_id: int | None = Field(default=None, foreign_key="score.id")

    # Relations
    vehicle: Vehicle | None = Relationship(back_populates="drivers")
    hours: Hours | None =  Relationship(back_populates="drivers")
    user: User | None = Relationship(back_populates="drivers")
    score: Score | None = Relationship(back_populates="drivers")

    # Fields
    date_drivers_license: date
    date_ID: date
    is_occupied: bool

