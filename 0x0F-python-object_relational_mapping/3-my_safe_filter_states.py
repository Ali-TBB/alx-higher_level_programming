#!/usr/bin/python3
"""
Script to list all states from a MySQL database with upper N.
Usage:
    python script.py <username> <password> <database>
"""


import MySQLdb
import sys


def search_states_by_name(username, password, database, state_name):
    """
    Function to search for states by name in the database
    (safe from MySQL injection).

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)

    # Create a cursor object
    cursor = db.cursor()

    query = """SELECT * FROM states WHERE name = '{}'
             ORDER BY id ASC""".format(state_name)
    cursor.execute(query)

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states_by_name(username, password, database, state_name)
