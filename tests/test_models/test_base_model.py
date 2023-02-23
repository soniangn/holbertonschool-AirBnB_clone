#!/usr/bin/python3
"""Test class base"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """Class test base"""

    def test_name(self):
        self.assertEqual(str, type(self.base.name))

    """Test of save"""
    def save(self):
        base = BaseModel()
        base.save()
        base.storage.new(self)


if __name__ == '__main__':
    unittest.main()
