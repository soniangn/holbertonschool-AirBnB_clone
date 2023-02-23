#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models import storage
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class Test_Base(unittest.TestCase):
    """Base class tests"""

    def test__file_path(self):
        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_reload(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_all(self):
        self.assertEqual(FileStorage._FileStorage__objects, storage.all())

if __name__ == '__main__':
    unittest.main()
