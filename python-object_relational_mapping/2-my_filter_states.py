#!/usr/bin/python3
"""
The "2. Filter states by user input" module
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         charset='utf8'
                         )
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY id ASC""".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
