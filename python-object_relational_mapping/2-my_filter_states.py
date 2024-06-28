#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query with user input
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)
        results = cursor.fetchall()

        # Print results
        for row in results:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.cl
