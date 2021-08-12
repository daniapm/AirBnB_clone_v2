#!/usr/bin/python3
""" Module for testing file storage"""
import models
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
import json
import os
import pep8
import unittest
import os
DBStorage = db_storage.DBStorage


class testDBStorage(unittest.TestCase):
    """ Class to test the file db_storage method """

    def test_pep8_base(self):
        """ test pep8 style"""
        self.assertEqual(os.system('pep8 models/engine/db_storage.py'), 0)
    
    def test_filename(self):
        """test that check file name"""
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(DBStorage.__doc__) > 1)
        self.assertTrue(len(DBStorage.__init__.__doc__) > 1)
        self.assertTrue(len(DBStorage.all.__doc__) > 1)
        self.assertTrue(len(DBStorage.save.__doc__) > 1)
        self.assertTrue(len(DBStorage.new.__doc__) > 1)
        self.assertTrue(len(DBStorage.delete.__doc__) > 1)
        self.assertTrue(len(DBStorage.reload.__doc__) > 1)

        @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "if storage is not dbstorage")
        def test_all(self):
            """check that all returns a dictionaty"""
            object = self.storage.all()
            self.assertIs(type(object), dict)

        @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') !='Filestorage', "if storage is filestorage")
        def test_new(self):
            """test new"""
            self.storage.new(State(name="Holbies"))
            self.assertIn(State(name="Holbies"), list(self.storage._DBStorage__session.new))
