#!/usr/bin/python3
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker, Session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from sqlalchemy.orm import scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                        .format(getenv("HBNB_MYSQL_USER"), cgetenv("HBNB_MYSQL_USER"),
                                        getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
                                        pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        if cls is not None:
            for key in self.__session.query(cls).all:
                new_dict[key.__class__.__name__ + "." + key.id] = key
            return new_dict

        else:
            for key in (self.__session.query(User).all)
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in(self.__session.query(State).all)
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in (self.__session.query(City).all)
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in (self.__session.query(Place).all)
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in (self.__session.query(Review).all)
                new_dict[key.__class__.__name__ + "." + key.id] = key
            return new_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__Session = scoped_session(session_factory)
        self.__Session = Session()

        Session.close()
