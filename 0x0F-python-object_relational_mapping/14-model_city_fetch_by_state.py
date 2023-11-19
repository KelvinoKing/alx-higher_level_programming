#!/usr/bin/python3
"""Import SQLAlchemy module
Base and State from model_state
"""
from model_state import Base, State
from model_city import City
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_cities_by_state(user, password, database):
    """lists cities by state
    """

    engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(user, password, database))

    Session = sessionmaker(bind=engine)

    try:
        session = Session()

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print("{}: ({}) {}".format(
                city.state.name, city.id, city.name))

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

    list_cities_by_state(username, encoded_password, database)
