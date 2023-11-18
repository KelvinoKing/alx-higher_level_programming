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
        if len(sys.argv) != 5:
            print("Requires 4 arguments")
            sys.exit(0)

        username, password, database, name = sys.argv[1:5]

        if not re.match(r'^[a-zA-Z0-9_]*$', database):
            raise ValueError("Invalid database name")

        with MySQLdb.connect(
                host="localhost", port=3306, user=username,
                passwd=password, db=database) as db:

            with db.cursor() as cur:
                query = "SELECT cities.name FROM cities INNER JOIN states \
                        ON states.id = cities.state_id \
                        WHERE states.name LIKE BINARY '%{}%' \
                        ORDER BY cities.id ASC;".format(name)
                cur.execute(query)
                print(', '.join([row[0] for row in cur.fetchall()]))

    except MySQLdb.Error as e:
        print("MySQLdb Error[%d]: %s" % (e.args[0], e.args[1]))
    except Exception as e:
        print("An error occured:", e)
