#!/usr/bin/python3
"""Import SQLAlchemy module
Base and State from model_state
"""
from model_state import Base, State
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_states_with_a(user, password, database):
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
        states_with_a = session.query(State).filter(State.name.ilike(
            '%a%')).order_by(State.id).all()

        if states_with_a:
            for state in states_with_a:
                print("{}: {}".format(state.id, state.name))

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

    list_states_with_a(username, encoded_password, database)
