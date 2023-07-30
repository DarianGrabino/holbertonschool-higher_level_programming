#!/usr/bin/python3
"""Filter states by user input"""
from sys import argv
import MySQLdb


def lists_states():
    """displays all values of database where name matches the argument"""

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %s", (argv[4],)
        # %s technique parametrización de consultas to avoid sql injection
    )
    result = cursor.fetchall()
    for row in result:
        print(row)


if __name__ == "__main__":
    lists_states()
