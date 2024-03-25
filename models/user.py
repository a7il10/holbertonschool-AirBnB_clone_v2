#!/usr/bin/python3
"""This is the user class"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import backref, relationship
from os import getenv

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref="user",
                           cascade="all, delete, delete-orphan")

        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""