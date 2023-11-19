#!/usr/bin/python3
"""Import SQLAlchemy module
Base and State from model_state
"""
from model_state import Base, State
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def get_state_id(user, password, database, state_name):
    """prints the state's id and state's name of state in table
    with 'a' character in their name

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
        state = session.query(State).filter(
                State.name == state_name).first()

        if state:
            print("{}".format(state.id))
        else:
            print("Not found")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Requires 4 arguments")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    encoded_password = quote(password, safe='')

    get_state_id(username, encoded_password, database, state_name)
