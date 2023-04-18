#!/usr/bin/python3
"""  lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa """
import sys
import MySQLdb


def ls_states(usr, ps, d):
    """ return contents of all states in hbtn_0e_0_usa"""
    h = 'localhost'
    ports = 3306
    db = MySQLdb.connect(host=h, user=usr, passwd=ps, db=d, port=ports)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE
                    BINARY 'N%' ORDER BY id ASC""")
    out = cur.fetchall()
    cur.close()
    db.close()
    return out


if __name__ == '__main__':

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    rows = ls_states(arg1, arg2, arg3)
    for row in rows:
        print(row)
