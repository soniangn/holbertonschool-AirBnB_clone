#!/usr/bin/python3
""" File Storage Unit tests """

from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import models
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """Class test FileStorage"""
    def test__file_path(self):
        """ Test of __file_path """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all(self):
        """ Test of all method """
        self.assertIs(FileStorage._FileStorage__objects, FileStorage.all)

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_reload(self):
        """Test of reload()"""
        with self.assertRaises(TypeError):
            FileStorage.reload(None)

    def test_save(self):
        """Test of save"""
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            self.assertEqual(dict, type(json.load(f)))
