from sqlmodel import Field, SQLModel, create_engine

# Those models will be eventually moved to another file, once I get it running

class Ticket(SQLModel, table=True):
    id_ticket: int | None = Field(default=None, primary_key=True)
    # id_user         FK
    # id_ticket_type  Enum
    # id_ticket_state Enum
    description: str

class User(SQLModel, table=True):
    id_user: int | None = Field(default=None, primary_key=True)
    # id_user_type    Enum
    name: str
    surename: str
    phone: str
    email: str
    gender: int  # Could be an Enum
    pay: float

class Order(SQLModel, table=True):
    id_order: int | None = Field(default=None, primaty_key=True)
    # id_address:     FK
    # id_restaurant:  FK
    # id_ticket:      FK
    # id_status:      Enum
    price: float
    # order_date:     Date
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
    # id_restaurant   FK
    name: str
    description: str
    # alergens: str
    price: float
