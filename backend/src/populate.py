from models import User, UserType, Gender, Food, Address, VehicleType, Vehicle, Hours, Score, Restaurant, Driver, Ticket, TicketType, TicketState, Order, OrderStatus, OrderHistory, AddressList, FoodOrder
from sqlmodel import Session
from datetime import time, date, datetime
import raw_forenames as forenames
import raw_surenames as surenames
import raw_cities as cities
import raw_postal_codes as postal_codes
import raw_street_names as street_names
import raw_food as food
import raw_vehicle_names as vehicle_names
import raw_vehicle_brands as vehicle_brands
import raw_vehicle_models as vehicle_models
import raw_restaurant_names as restaurant_names
import random


def populate(engine):
    with Session(engine) as session:
        # Arrays for later linking
        _addresses: list[Address] = []
        _address_list: list[AddressList] = []
        _drivers: list[Driver] = []
        _food: list[Food] = []
        _food_orders: list[FoodOrder] = []
        _hours: list[Hours] = []
        _orders: list[Order] = []
        _order_history: list[OrderHistory] = []
        _restaurants: list[Restaurant] = []
        _scores: list[Score] = []
        _tickets: list[Ticket] = []
        _users: list[User] = []  # This is for later linking relations with other tablesi
        _vehicles: list[Vehicle] = []
        _vehicle_types: list[VehicleType] = []
        # Filling tables
        # Users
        for _ in range(200):
            _forename = random.choice(forenames.forenames)
            _surename = random.choice(surenames.surenames)
            _user = User(
                user_type=UserType.USER,  # TODO Make it random to a certain degree
                name= _forename,
                surename= _surename,
                phone=gen_phone(),
                email='{}.{}@elozelo.pl'.format(_forename, _surename),
                gender=rand_gender(),
                pay=random.random() * 1000.0  # Wiem że wartości dość abstrakcyjne
            )
            session.add(_user)
            _users.append(_user)
        # Addresses
        for _ in range(100):
            _address = Address(
                city=random.choice(cities.cities),
                street=random.choice(street_names.street_names),
                zip_code=random.choice(postal_codes.postal_codes),
                house_number=random.randint(1, 200),
                apartment_number=random.randint(1, 50)
            )
            session.add(_address)
            _addresses.append(_address)
        # Vehicle Types
        for _vehicle_name in vehicle_names.vehicle_names:
            _vehicle_type = VehicleType(
                name=_vehicle_name,
                max_weight=random.random() * 5000.0
            )
            session.add(_vehicle_type)
            _vehicle_types.append(_vehicle_type)
        # Vehicles (must be done after vehicle types exist)
        for _ in range(100):
            _vehicle = Vehicle(
                model=random.choice(vehicle_models.vehicle_models),
                brand=random.choice(vehicle_brands.vehicle_brands),
                vehicle_type=random.choice(_vehicle_types)
            )
            session.add(_vehicle)
            _vehicles.append(_vehicle)
        # Hours
        for _ in range(300):
            _from = time(random.randint(0, 23), random.randint(0, 59))
            _to = time(random.randint(0, 23), random.randint(0, 59))
            _hour = Hours(
                time_from=_from,
                time_t=_to,
                day="We didn't agree on this after all. Don't use this. I think that this is a good place for an enum"
            )
            session.add(_hour)
            _hours.append(_hour)
        # Scores
        for _ in range(200):
            _score = Score(
                amount=random.randint(0, 10),
                sum=0.0
            )
            session.add(_score)
            _scores.append(_score)
        # Restarans
        for _restauran_name in restaurant_names.restaurant_names:
            _restaurant = Restaurant(
                hours=random.choice(_hours),
                score=random.choice(_scores),
                name=_restauran_name,
                pay_cut=random.random(),
                email="{}@restaurant.pl".format(
                    _restauran_name.lower().replace(" ", ".")
                ),
                phone=gen_phone()
            )
            session.add(_restaurant)
            _restaurants.append(_restaurant)
        # Food
        for _restaurant in _restaurants:
            for _ in range(random.randint(5, 10)):
                _f = Food(  # _food was already taken, so here is _f
                    restaurant=random.choice(_restaurants),
                    price=random.random() * 100.0,
                    name=random.choice(food.food),
                    description="No description provided"
                )
                session.add(_f)
                _food.append(_f)
        # for food_name in food.food:
        #     _f = Food(  # _food was already taken, so here is _f
        #         restaurant=random.choice(_restaurants),
        #         price=random.random() * 100.0,
        #         name=food_name,
        #         description="No description provided"
        #     )
        #     session.add(_f)
        #     _food.append(_f)
        # Drivers
        for _ in range(80):
            _u = random.choice(_users)
            _u.user_type = UserType.DRIVER
            session.add(_u)
            _driver = Driver(
                vehicle=random.choice(_vehicles),
                hours=random.choice(_hours),
                user=_u,
                score=random.choice(_scores),
                date_drivers_license=gen_date(),
                date_ID=gen_date(),
                is_occupied=False 
            )
            session.add(_driver)
            _drivers.append(_driver)
        # Tickets
        for _ in range(200):
            _ticket = Ticket(
                user=random.choice(_users),
                ticket_type=random.choice(list(TicketType)),
                ticket_state=random.choice(list(TicketState)),
                description="No description"
            )
            session.add(_ticket)
            _tickets.append(_ticket)
        # Orders
        for _ in range(150):
            _d = gen_date()
            _order = Order(
                address=random.choice(_addresses),
                restaurant=random.choice(_restaurants),
                tickets=random.choice(_tickets),
                status=random.choice(list(OrderStatus)),
                price=random.random() * 1000.0,
                order_date=datetime(
                    _d.year,
                    _d.month,
                    _d.day,
                    random.randint(0, 23),
                    random.randint(0, 59)
                ),
                weight=random.random() * 100.0,
                score_driver=random.random() * 10.0,
                score_restaurant = random.random() * 10.0
            )
            session.add(_order)
            _orders.append(_order)
        # OrderHistory
        for _ in range(400):
            _historical_order = OrderHistory(
                order=random.choice(_orders),
                user=random.choice(_users)
            )
            session.add(_historical_order)
            _order_history.append(_historical_order)
        # AddressList
        for _ in range(250):
            _address_in_list = AddressList(
                user=random.choice(_users),
                address=random.choice(_addresses)
            )
            session.add(_address_in_list)
            _address_list.append(_address_in_list)
        # FoodOrders
        for _ in range(600):
            _food_order = FoodOrder(
                food=random.choice(_food),
                order=random.choice(_orders),
                quantity=random.randint(1, 25)
            )
            session.add(_food_order)
            _food_orders.append(_food_order)
        session.commit()


def gen_date() -> date:
    try:
        return date(
            random.randint(1980, 2060),
            random.randint(1, 12),
            random.randint(1, 31)
        )
    except:
        return date(
            random.randint(1980, 2060),
            random.randint(1, 12),
            1
        )


def gen_phone(phone_number_length=9) -> str:
    return ''.join([str(random.randint(0, 9)) for _ in range(phone_number_length)])


def rand_gender() -> Gender:
    # The logic here goes as follow
    # 1 - 5 -> Female
    # 6 - 10 -> Male
    # 11 and 12 -> Unknown
    # 13 -> Other
    _r = random.randint(1, 13)
    if 1 <= _r <= 5:
        return Gender.FEMALE
    elif 6 <= _r <= 10:
        return Gender.MALE
    elif _r == 11 or _r == 12:
        return Gender.UNSPECIFIED
    elif _r == 13:
        return Gender.OTHER
    return Gender.UNSPECIFIED

