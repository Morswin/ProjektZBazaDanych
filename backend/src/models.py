from datetime import date, time, datetime
from enum import Enum
from sqlmodel import Field, SQLModel, Relationship


# It must be declared befor user and order for some reason. Otherwise the IDE spams with errors.
class OrderHistory(SQLModel, table=True):
    __tablename__ = "order_history"

    # Keys
    id_order: int | None = Field(default=None, foreign_key="order.id_order", primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id_user", primary_key=True)


class AddressList(SQLModel, table=True):
    __tablename__ = "address_list"

    #keys
    id_user: int | None = Field(default=None, foreign_key="user.id_user", primary_key=True)
    id_address: int | None = Field(default=None, foreign_key="address.id_address", primary_key=True)


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
    __tablename__ = "user"

    # Keys
    id_user: int | None = Field(default=None, primary_key=True)

    # Relations
    orders: list["Order"] = Relationship(back_populates="users", link_model=OrderHistory)
    tickets: list["Ticket"] = Relationship(back_populates="user")

    # Fields
    user_type: UserType
    name: str
    surename: str
    phone: str
    email: str
    gender: Gender
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
    id_ticket: int | None = Field(default=None, primary_key=True)

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
    id_address: int | None = Field(default=None, primary_key=True)

    # Relations
    orders: list["Order"] = Relationship(back_populates="address")

    # Fields
    city: str
    street: str
    zip_code: str
    house_number: int
    apartment_number: int


class Restaurant(SQLModel, table=True):
    __tablename__ = "restaurant"

    # Keys
    id_restaurant: int | None = Field(default=None, primary_key=True)
    id_hours: int | None = Field(default=None, foreign_key="hours.id_hours")
    id_score: int | None = Field(default=None, foreign_key="score.id_score")

    # Relations
    orders: list["Order"] = Relationship(back_populates="restaurant")

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
    id_order: int | None = Field(default=None, primary_key=True)

    # Relations
    users: list["User"] = Relationship(back_populates="orders", link_model=OrderHistory)
    address: Address | None = Relationship(back_populates="orders")
    restaurant: Restaurant | None = Relationship(back_populates="orders")
    ticket: Ticket | None = Relationship(back_populates="orders")

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
    id_food: int | None = Field(default=None, primary_key=True)
    id_restaurant: int | None = Field(default=None, foreign_key="restaurant.id_restaurant")

    # Fields
    name: str
    description: str
    # alergens: str  # For now we will not implement this. It may be a separate table with a many to many relation.
    price: float


class VehicleType(SQLModel, table=True):
    __tablename__ = "vehicle_type"

    # Keys
    id_vehicle_type: int | None = Field(default=None, primary_key=True)

    # Relations
    vehicles: list["Vehicle"] = Relationship(back_populates="vehicle_type")

    # Fields
    name: str
    max_weight: float  # How much it can carry in it's cargo or such


class Vehicle(SQLModel, table=True):
    __tablename__ = "vehicle"

    # Keys
    id_vehicle: int | None = Field(default=None, primary_key=True)

    # Relations
    drivers: list["Driver"] = Relationship(back_populates="vehicle")
    vehicle_type: VehicleType | None = Relationship(back_populates="vehicles")

    # Fields
    brand: str
    model: str


class Hours(SQLModel, table=True):
    __tablename__ = "hours"

    # Keys
    id_hours: int | None = Field(default=None, primary_key=True)

    # Fields
    day: str  # Let's rediscuss if Varchar makes sense here, but for now it stays
    time_from: time
    time_t: time


class Score(SQLModel, table=True):
    __tablename__ = "score"

    # Keys
    id_score: int | None = Field(default=None, primary_key=True)

    # Fields
    amount: int
    sum: float


class Driver(SQLModel, table=True):
    __tablename__ = "driver"

    # Keys
    id_driver: int | None = Field(default=None, primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id_user")
    id_hours: int | None = Field(default=None, foreign_key="hours.id_hours")
    id_score: int | None = Field(default=None, foreign_key="score.id_score")

    # Relations
    vehicle: Vehicle | None = Relationship(back_populates="drivers")    

    # Fields
    date_drivers_license: date
    date_ID: date
    is_occupied: bool

