#!/usr/bin/python3
"""Import SQLAlchemy modules
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class

    Attributes
    id (int): auto-generated
    name (str): name of state
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade="all, delete-orphan", back_populates="state")
