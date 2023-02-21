#!/usr/bin/python3
"""Test class base"""

import unittest
from models.base_model import BaseModel


class FileStorage(unittest.TestCase):
    """Class test FileStorage"""

    """Test of __file_path:"""
    def test_file_path(self):
        file = FileStorage()
        self.assertEqual(file._FileStorage__file_path, "file.json")

    """Test of __objects"""
    """def test_objects(self):
        file = FileStorage()"""

    """Test of all()"""
    """def test_all(self):
        FileStorage.all"""

    """Test of new()"""
    """def test_new(self):
        FileStorage.new()"""

    """Test of save()"""
    """def test_safe(self):
        FileStorage.safe()"""

    """Test of reload()"""
    """def test_reload(self):
        with self.assertRaises(TypeError):
            FileStorage.reload(None)

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))"""


if __name__ == '__main__':
    unittest.main()
