#!/usr/bin/python3
"""All states via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


def lists_states():
    """lists all states"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )
    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == '__main__':
    lists_states()
