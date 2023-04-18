#!/usr/bin/python3
""" lists all the states contained in the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def all_states(usr, ps, d):
    """ returns contents of the states table"""
    ports = 3306
    h = 'localhost'
    db = MySQLdb.connect(host=h, user=usr, passwd=ps, db=d, port=ports)
    cur = db.cursor()
    cur.execute(" SELECT * FROM states")
    info = cur.fetchall()
    cur.close()
    db.close()
    return info


if __name__ == '__main__':

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    rows = all_states(arg1, arg2, arg3)
    for info in rows:
        print(info)
