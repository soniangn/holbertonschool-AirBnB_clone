#!/usr/bin/python3
"""Test class base"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Class test base"""

    """Test of Base() for assigning automatically an ID exists"""
    def test_id(self):
        base = BaseModel()
        self.assertEqual(base.id, 1)

    """Test of Base(89) saving the ID passed exists"""
    def test_id_pass(self):
        my_number = BaseModel(89)
        self.assertEqual(my_number, 89)

    """Base.from_json_string"""
    """All test validate from Json string"""
    def test_exist(self):
        self.assertTrue(os.path.exists("file.json"))

    """Test of save"""
    def save(self):
        base = BaseModel()
        base.save()
        base.storage.new(self)


if __name__ == '__main__':
    unittest.main()
