#!/usr/bin/python3
"""Import SQLAlchemy module
Base and State from model_state
"""
from model_state import Base, State
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_first_state(user, password, database):
    """prints the state's id and state's name of first state in table

    parameters:
        user (string): username
        password (string): user passsword
        database (string): name of database
    """

    engine = create_engine(
            "mysql://{}:{}@localhost:3306/{}".format(user, password, database))

    Session = sessionmaker(bind=engine)

    try:
        session = Session()
        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            pass

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

    list_first_state(username, encoded_password, database)
