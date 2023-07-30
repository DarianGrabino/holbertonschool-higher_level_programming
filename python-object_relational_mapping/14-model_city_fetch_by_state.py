#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import create_engine
from model_state import Base, City


def add_states():
    """Add a new state"""
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
        )
    result = engine.execute('SELECT states.name, cities.id, cities.name \
                            FROM cities, states \
                            WHERE states.id = cities.state_id')
    rows = result.fetchall()
    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
    result.close()


if __name__ == '__main__':
    add_states()
