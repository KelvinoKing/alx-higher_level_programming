#!/usr/bin/python3
"""MySQLdb module
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    import re

    db = None
    cur = None

    try:
        if len(sys.argv) != 4:
            print("Requires 4 arguments")
            sys.exit(0)

        username, password, database = sys.argv[1:4]

        if not re.match(r'^[a-zA-Z0-9_]*$', database):
            raise ValueError("Invalid database name")

        with MySQLdb.connect(
                host="localhost", port=3306, user=username,
                passwd=password, db=database) as db:

            with db.cursor() as cur:
                query = "SELECT cities.id, cities.name, states.name \
                        FROM cities INNER JOIN states \
                        ON states.id = cities.state_id \
                        ORDER BY cities.id ASC;"
                cur.execute(query)
                AllInfo = cur.fetchall()
                for info in AllInfo:
                    print(info)

    except MySQLdb.Error as e:
        print("MySQLdb Error[%d]: %s" % (e.args[0], e.args[1]))
    except Exception as e:
        print("An error occured:", e)
