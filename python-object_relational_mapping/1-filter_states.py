#!/usr/bin/python3
"""Filter states"""
from sys import argv
import MySQLdb


def lists_states():
    """ lists all states with a name starting with N from the database """

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for row in result:
        if row[1].startswith("N"):
            print(row)


if __name__ == "__main__":
    lists_states()
