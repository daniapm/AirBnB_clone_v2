#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.engine.db_storage import DBStorage


class test_DBStorage(unittest.TestCase):
    """ Class to test the file db_storage method """

    def test_pep8_base(self):
        """ test pep8 style"""
        self.assertEqual(os.system('pep8 models/engine/db_storage.py'), 0)

    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(DBStorage.__doc__) > 1)
        self.assertTrue(len(DBStorage.__init__.__doc__) > 1)
        self.assertTrue(len(DBStorage.all.__doc__) > 1)
        self.assertTrue(len(DBStorage.save.__doc__) > 1)
        self.assertTrue(len(DBStorage.new.__doc__) > 1)
        self.assertTrue(len(DBStorage.delete.__doc__) > 1)
        self.assertTrue(len(DBStorage.reload.__doc__) > 1)
