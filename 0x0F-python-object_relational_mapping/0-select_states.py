#!/usr/bin/python3
"""MySQLdb module
"""
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Requires 4 arguments")
    exit(0)
else:
    try:
        db = MySQLdb.connect(
                host=sys.argv[1], port=3306, user=sys.argv[2],
                passwd=sys.argv[3], db="hbtn_0e_0_usa")

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY `id` ASC")
        allInfo = cur.fetchall()
        for info in allInfo:
            print(info)
    except MySQLdb.Error as e:
        print("MySQL Error[%d]: %s" % (e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
