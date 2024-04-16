#!/usr/bin/python3

"""
Script to list all states from a MySQL database with upper N.
Usage:
    python script.py <username> <password> <database>
"""


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))


    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
