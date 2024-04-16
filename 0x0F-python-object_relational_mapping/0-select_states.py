#!/usr/bin/python3
"""
Script to list all states from a MySQL database.
Usage:
    python script.py <username> <password> <database>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost",user=username, passwd=password,
                     db=database, port=3306)

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
