#!/usr/bin/python3
"""Test class base"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine import storage


class FileStorage(unittest.TestCase):
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
        """ delete json file at the end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    """Test of __file_path:"""
    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(storage.FileStorage.__file_path, "file.json")

    def test_all(self):
        """Test of all()"""
        storage = FileStorage()
        all_obj = storage.all()
        self.assertIs(all_obj, storage.FileStorage__objects)

    def test_new(self):
        """Test of new()"""

    

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
