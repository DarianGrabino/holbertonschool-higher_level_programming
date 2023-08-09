#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
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
    states_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_delete:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    add_states()
