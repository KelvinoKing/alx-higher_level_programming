#!/usr/bin/python3
"""Script that lists all State objects and corresponding
City objects in the database hbtn_0e_101_usa
"""

import sys
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_states_cities(user, password, database):
    """Lists all State objects and corresponding
    City objects in the specified database
    """

    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(
        user, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    try:
        session = Session()

        # Query all State objects with their linked City objects
        states = session.query(State).order_by(State.id).all()

        for state in states:
            print("{}: {}".format(state.id, state.name))

            # Use a tabulation for each City
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Requires 4 arguments")
        sys.exit(1)

    username, password, database = sys.argv[1:4]
    encoded_password = quote(password, safe='')
    list_states_cities(username, encoded_password, database)
