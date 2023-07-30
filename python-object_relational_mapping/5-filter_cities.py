#!/usr/bin/python3
"""All cities by states"""
from sys import argv
import MySQLdb


def lists_states():
    """ lists all cities by satates from the database """

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name, states.name \
        FROM cities, states \
        WHERE state_id = states.id \
        AND states.name = %s", (argv[4],)
    )
    result = cursor.fetchall()
    cities = []
    for row in result:
        cities.append(row[0])
    print(", ".join(cities))


if __name__ == "__main__":
    lists_states()
