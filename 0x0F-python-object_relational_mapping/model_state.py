#!/usr/bin/python3
"""
module that contains class definitions of a State and an
instance Base
"""


from sqlalchemy import (
    inspect,
    Column,
    String,
    Integer
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class definitions id and name"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
