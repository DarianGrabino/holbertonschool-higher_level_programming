#!/usr/bin/python3
"""All states via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State


def lists_states():
    """print first state"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )
    connection = engine.connect()
    result = connection.execute('SELECT * FROM states')
    first_elem = result.fetchone()
    if first_elem is None:
        print('Nothing')
    else:
        print(f"{first_elem[0]}: {first_elem[1]}")


if __name__ == '__main__':
    lists_states()
