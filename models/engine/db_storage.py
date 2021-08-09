#!/usr/bin/python3
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker

class DBStorage:
	__engine = None
	__session = None
	
	def __init__(self):
		self.__engine = create_engine ('mysql+mysqldb://{}:{}@localhost/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_DB)), pool_pre_ping=True)
		
	@property
    def session(self):
        return self.__session

   	@session.setter
    def get_session(self, value):
		self.__session = value

	__session = sessionmaker(bind=__engine)
    __Session = Session()


		