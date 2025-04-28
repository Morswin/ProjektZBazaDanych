from models import User, UserType, Gender
from sqlmodel import Session
import raw_forenames as forenames
import raw_surenames as surenames
import random


def populate(engine):
    session = Session(engine)
    for _ in range(100):
        _user = User(
            user_type=UserType.USER,
            name=random.choice(forenames.forenames),
            surename=random.choice(surenames.surenames),
            phone=''.join([str(range(0, 10)) for i in range(9)]),
            email='elo@zelo.pl',
            gender=Gender.FEMALE,
            pay=21.37
        )
        session.add(_user)
    session.commit()

