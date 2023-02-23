#!/usr/bin/python3
""" File Storage Unit tests """

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Class test FileStorage"""

    def test_file_path(self):
        """ Test of __file_path """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all(self):
        """ Test of all method """
        self.assertIs(FileStorage._FileStorage__objects, storage.all)

    def test_reload(self):
        """Test of reload()"""
        with self.assertRaises(TypeError):
            FileStorage.reload(None)

    def test_safe(self):
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            self.assertEqual(dict, type(json.load(f)))


if __name__ == '__main__':
    unittest.main()

