#!/usr/bin/python3
""" Unittest for User """
import unittest
from models.base_model import BaseModel
from models.user import User
import os

#!/usr/bin/python3
"""Test cases for User Class"""

class TestUser(unittest.TestCase):
    """ test User """
    def setUp(self):
        """ creates an instance of User with attributes """
        self.user = User()
        self.user.first_name = "Vanessa"
        self.user.last_name = "Tessier"
        self.user.password = "sTr@n_G"
        self.user.email = "vt@mail.com"

    @classmethod
    def tearDownClass(cls):
        """ delete json file at the end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_user(self):
        """ checks user's attributes """
        self.assertEqual(str, type(self.user.first_name), "Vanessa")
        self.assertEqual(str, type(self.user.last_name), "Tessier")
        self.assertEqual(str, type(self.user.password), "sTr@n_G")
        self.assertEqual(str, type(self.user.email), "vt@mail.com")


if __name__ == '__main__':
    unittest.main
