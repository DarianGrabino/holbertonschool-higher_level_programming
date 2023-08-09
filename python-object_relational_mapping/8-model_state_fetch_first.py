#!/usr/bin/python3
"""All states via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def lists_states():
    """print first state"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).first()
    if first_state is None:
        print('Nothing')
    else:
        print(f"{first_state.id}: {first_state.name}")


if __name__ == '__main__':
    lists_states()
