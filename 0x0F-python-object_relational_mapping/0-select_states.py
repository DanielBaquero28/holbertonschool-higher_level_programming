#!/usr/bin/python3
import MySQLdb
from sys import argv as av

if __name__ == '__main__':
    """ Lists all states from the database hbtn_0e_0_usa """
    db = MySQLdb.connect(user=av[1], passwd=av[2], db=av[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM staetes')
    for record in cursor.fetchall():
        print(record)

    cursor.close()
    db.close()
