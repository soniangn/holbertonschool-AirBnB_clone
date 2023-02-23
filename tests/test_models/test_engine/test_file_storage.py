#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models import storage
import pep8
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_Base(unittest.TestCase):
    """Base class tests"""

    def test__file_path(self):
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_reload(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_all(self):
        self.assertEqual(FileStorage._FileStorage__objects, storage.all())

    def test_save(self):
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            self.assertEqual(dict, type(json.load(f)))

    def pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        print = "Found code style errors"
        self.assertEqual(result.total_errors, 0, print)

if __name__ == '__main__':
    unittest.main()