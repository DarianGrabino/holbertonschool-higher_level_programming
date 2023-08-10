#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


def add_states():
    """Add a new state"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    cities_states = session.query(City, State).join(State)\
        .order_by(City.id).all()
    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == '__main__':
    add_states()
