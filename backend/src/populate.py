from models import User, UserType, Gender, Food, Address, VehicleType, Vehicle, Hours, Score
from sqlmodel import Session
from datetime import time
import raw_forenames as forenames
import raw_surenames as surenames
import raw_cities as cities
import raw_postal_codes as postal_codes
import raw_street_names as street_names
import raw_food as food
import raw_vehicle_names as vehicle_names
import raw_vehicle_brands as vehicle_brands
import raw_vehicle_models as vehicle_models
import random


def populate(engine):
    with Session(engine) as session:
        # Arrays for later linking
        _addresses: list[Address] = []
        _food: list[Food] = []
        _hours: list[Hours] = []
        _scores: list[Score] = []
        _users: list[User] = []  # This is for later linking relations with other tablesi
        _vehicles: list[Vehicle] = []
        _vehicle_types: list[VehicleType] = []
        # Filling tables
        # Users
        for _ in range(100):
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
        # Food
        for food_name in food.food:
            _f = Food(  # _food was already taken, so here is _f
                price=random.random() * 100.0,
                name=food_name,
                description="No description provided"
            )
            session.add(_f)
            _food.append(_f)
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
        for _ in range(40):
            _from = time()
            _from.hour = random.randint(0, 23)
            _to = time()
            _to.hour = random.randint(0, 23)
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
        session.commit()

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

