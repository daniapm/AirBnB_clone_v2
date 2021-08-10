#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    City = relationship("City")
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def city_get(self):
        """getter attribute cities
        """
        city_list = {}
        for i in FileStorage.all(City).items():
            if i in self.id:
                city_list[i] = FileStorage.all(City)
        return city_list
