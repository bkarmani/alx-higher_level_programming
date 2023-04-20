#!/usr/bin/python3
"""takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb


def ls_states(usr, p, d, state):
    h = 'localhost'
    ports = 3306
    db = MySQLdb.connect(host=h, user=usr, passwd=p, db=d, port=ports)
    cur = db.cursor()
    cur.execute(" SELECT * FROM states WHERE name = '{}' ".format(state))
    out = cur.fetchall()
    cur.close()
    db.close()
    return out


if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    arg4 = sys.argv[4]
    rows = ls_states(arg1, arg2, arg3, arg4)
    for row in rows:
        print(row)
