#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref=backref(
            "state", cascade="all, delete"))
    else:
        @property
        def get_cities(self):
            """the geter of cities"""
            from models.city import City
            objs = models.storage.all(City)
            list = []
            for city in objs.values():
                if city.state_id == self.id:
                    list.append(city)
            return list
