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

    for state in session.query(State).order_by(State.id):
        if state.name == sys.argv[4]:
            print(f"{state.id}")
            sys.exit()
    print("Not found")

    session.close()


if __name__ == '__main__':
    lists_states()
