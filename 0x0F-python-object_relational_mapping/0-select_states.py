#!/usr/bin/python3

import MySQLdb
import sys


def list_states(user, passwd, db):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=user, passwd=passwd, db=db, port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
