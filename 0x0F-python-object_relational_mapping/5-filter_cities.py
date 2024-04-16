#!/usr/bin/python3
"""
Script to list all cities from the database.
Usage:
    python script.py <username> <password> <database>
"""


import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """
    Function to list all cities from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

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

    sql = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""

    cursor.execute(sql, (state_name,))
    # Fetch all the rows
    data = cursor.fetchall()

    # Display the results
    print(", ".join([city[0] for city in data]))

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    list_cities(username, password, database, state_name)
