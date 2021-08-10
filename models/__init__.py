#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage
storage_type = getenv("HBNB_MYSQL_USER")

if getenv("HBNB_MYSQL_USER") == "db":
	from models.engine.db_storage import DBStorage
	new_storage = DBStorage()
	new_storage.reload()
else:
	storage = FileStorage()
	storage.reload()
