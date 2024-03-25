#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances with state_id"""
        list_cities = []
        for key, value in models.storage.all(City).items():
            if value.state_id == self.id:
                list_cities.append(value)
        return list_cities
