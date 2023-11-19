#!/usr/bin/python3
"""Import SQLAlchemy module
Base and State from model_state
"""
from relationship_state import Base, State
from relationship_city import City
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def create_california_san_francisco(user, password, database):
    """Adds a new state and prints its id
    """

    engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(user, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    try:
        session = Session()

        california = State(name="California")
        session.add(california)
        session.flush()

        san_francisco = City(name="San Francisco", state_id=california.id)
        session.add(san_francisco)
        session.commit()

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

    create_california_san_francisco(username, encoded_password, database)
