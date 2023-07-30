#!/usr/bin/python3
"""All states via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State


def lists_states():
    """lists all states"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )
    connection = engine.connect()
    result = connection.execute('SELECT * FROM states')
    for elem in result:
        print(f"{elem[0]}: {elem[1]}")


if __name__ == '__main__':
    lists_states()
