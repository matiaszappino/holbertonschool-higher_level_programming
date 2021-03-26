#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    STATE_NAME = argv[4]

    db = MySQLdb.connect(host='localhost',  user=MY_USER, passwd=MY_PASS, db=MY_DB, port=3306)
    cur = db.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name=%s) ORDER BY cities.id ASC", (STATE_NAME,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
