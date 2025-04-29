from models import User, UserType, Gender
from sqlmodel import Session
import raw_forenames as forenames
import raw_surenames as surenames
import random


def populate(engine):
    with Session(engine) as session:
        _users: list[User] = []  # This is for later linking relations with other tables
        for _ in range(100):
            _forename = random.choice(forenames.forenames)
            _surename = random.choice(surenames.surenames)
            _user = User(
                user_type=UserType.USER,
                name= _forename,
                surename= _surename,
                phone=gen_phone(),
                email='{}.{}@elozelo.pl'.format(_forename, _surename),
                gender=rand_gender(),
                pay=21.37
            )
            session.add(_user)
            _users.append(_user)
        session.commit()


def gen_phone(phone_number_length=9) -> str:
    return ''.join([str(random.randint(0, 9)) for _ in range(phone_number_length)])

def rand_gender() -> Gender:
    match random.randint(1, 4):
        case 1:
            return Gender.FEMALE
        case 2:
            return Gender.MALE
        case 3:
            return Gender.OTHER
        case 4:
            return Gender.UNSPECIFIED

