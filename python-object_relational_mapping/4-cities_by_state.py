#!/usr/bin/python3
"""Cities by states"""
from sys import argv
import MySQLdb


def lists_states():
    """ lists all cities from the database """

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT ROW_NUMBER() OVER(), cities.name,states.name \
        FROM cities, states WHERE state_id = states.id"
    )
    result = cursor.fetchall()
    for row in result:
        print(row)


if __name__ == "__main__":
    lists_states()
