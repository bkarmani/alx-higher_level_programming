#!/usr/bin/python3
import MySQLdb, sys
def all_states (username, password, db_name):
    ports = 3306
    db = MySQLdb.connect(host = 'localhost', user = username, passwd = password, db = db_name, port = ports)
    cur = db.cursor()
    cur.execute(" SELCT * FROM states")
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
