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
        self.user.first_name = "Vanessa"
        self.user.last_name = "Tessier"
        self.user.password = "sTr@n_G"
        self.user.email = "vt@mail.com"
        self.storage = FileStorage()

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
        FileStorage.save()

    """Test of reload()"""
    """def test_reload(self):
        with self.assertRaises(TypeError):
            FileStorage.reload(None)

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))"""


if __name__ == '__main__':
    unittest.main()

