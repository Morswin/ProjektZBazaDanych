from models import User, UserType, Gender
from sqlmodel import Session
import raw_forenames as forenames
import raw_surenames as surenames
import random


def populate(engine):
    session = Session(engine)
    for _ in range(100):
        _forename = random.choice(forenames.forenames)
        _surename = random.choice(surenames.surenames)
        _user = User(
            user_type=UserType.USER,
            name= _forename,
            surename= _surename,
            phone=''.join([i for i in range(9)]),
            email='{}.{}@elozelo.pl'.format(_forename, _surename),
            gender=Gender.FEMALE,
            pay=21.37
        )
        session.add(_user)
    session.commit()

