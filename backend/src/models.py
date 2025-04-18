import datetime
from sqlmodel import Field, SQLModel

# Those models will be eventually moved to another file, once I get it running

class Ticket(SQLModel, table=True):
    id_ticket: int | None = Field(default=None, primary_key=True)
    id_user: int | None = Field(default=None, foreign_key="user.id_user")
    # id_ticket_type        Enum
    # id_ticket_state       Enum
    description: str

class User(SQLModel, table=True):
    id_user: int | None = Field(default=None, primary_key=True)
    # id_user_type          Enum
    name: str
    surename: str
    phone: str
    email: str
    gender: int  # Could be an Enum
    pay: float

class Order(SQLModel, table=True):
    id_order: int | None = Field(default=None, primaty_key=True)
    id_address: int | None = Field(default=None, foreign_key="address.id_address")
    id_restaurant: int | None = Field(default=None, foreign_key="restaurant.id_restaurant")
    id_ticket: int | None = Field(default=None, foreign_key="ticket.id_ticket")
    # id_status:            Enum
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
    # alergens: str ???
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
    date_drivers_license: datetime
    date_ID: datetime
    is_occupied: bool

class Vehicle(SQLModel, table=True):
    id_vehicle: int | None = Field(default=None, primary_key=True)
    id_vehicle_type: int | None = Field(default=None, foreign_key="vehicletype.id_vehicle_type")
    brand: str
    model: str

class Vehicletype(SQLModel, table=True):
    id_veficle_type: int | None = Field(default=None, primary_key=True)
    name: str
    max_weight: float  # How much it can carry in it's cargo or such

class Hours(SQLModel, table=True):
    id_hours: int | None = Field(default=None, primary_key=True)
    day: str  # Let's rediscuss if Varchar makes sense here, but for now it stays
    time_from: datetime
    time_t: datetime

class Score(SQLModel, table=True):
    id_score: int | None = Field(default=None, primary_key=True)
    amount: int
    sum: float
