#!/usr/bin/python3
"""Import SQLAlchemy module
Base and State from model_state
"""
from model_state import Base, State
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def change_state_name(user, password, database):
    """Adds a new state and prints its id
    """

    engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(user, password, database))

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)

    try:
        session = Session()

        state_to_change = session.query(State).filter(State.id == 2).first()
        state_to_change.name = "New Mexico"
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

    change_state_name(username, encoded_password, database)
