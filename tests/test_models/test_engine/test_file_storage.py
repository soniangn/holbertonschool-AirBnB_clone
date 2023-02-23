#!/usr/bin/python3
""" File Storage Unit tests """

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class test FileStorage"""

    def setUp(self):
        """ creates an instance of User with attributes """
        self.user = User()

    @classmethod
    def tearDownClass(cls):
        """ deletes json file at the end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_file_path(self):
        """ Test of __file_path """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all(self):
        """ Test of all method """
        storage = FileStorage()
        all_obj = storage.all()
        self.assertIs(all_obj, storage._FileStorage__objects)

    """Test of save()"""
    def test_save(self):
        storage = FileStorage()
        self.user = User()
        storage.save()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    """Test of reload()"""
    def test_reload(self):
        with self.assertRaises(TypeError):
            FileStorage.reload(None)

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))"""


if __name__ == '__main__':
    unittest.main()

