#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
import models
from os import getenv
from sqlalchemy import *

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref=backref(
            "place", cascade="all, delete"))
        amenities = relationship("Amenity", secondary=
                                place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """the geter of reviews"""
            from models.review import Review
            objs = models.storage.all(Review)
            list = []
            for review in objs.values():
                if review.place_id == self.id:
                    list.append(review)
            return list
        
        @property
        def amenities(self):
            """the geter of amenities"""
            from models.amenity import Amenity
            objs = models.storage.all(Amenity)
            list = []
            for amenity in objs.values():
                if amenity.place_id == self.id:
                    list.append(amenity)
            return list

        @amenities.setter
        def amenities(self, object):
            """the setter of amenities"""
            from models.amenity import Amenity
            if object == "Amenity":
                self.amenity_ids.append(object)
