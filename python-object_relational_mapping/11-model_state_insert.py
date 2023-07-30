#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


def add_states():
    """Add a new state"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )
    session = Session(engine)
    session.add(State(name='Louisiana'))
    session.commit()
    result = session.query(State).order_by(State.id.desc()).first()
    print(result.id)

    session.close()


if __name__ == '__main__':
    add_states()
