#!/usr/bin/python3
"""Defines unittests for console.py."""
from models.engine.file_storage import FileStorage
import unittest
import pep8
import json
import os
from models.user import User
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Testing instantiation of the FileStorage class."""
    storage = FileStorage()
    path = storage._FileStorage__file_path

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_pep8_base(self):
        """ test pep8 style"""
        self.assertEqual(os.system('pep8 console.py'), 0)
    
    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(HBNBCommand.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.__init__.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.help_destroy.__doc__) > 1)
