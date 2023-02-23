#!/usr/bin/python3
"""Test class base"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import uuid

class TestBaseModel(unittest.TestCase):
    """Class test base"""

    def setUp(self):
        """ creates an instance of BaseModel """
        self.base = BaseModel()
        self.base.name = "BaseModel"
        self.base.id = str(uuid.uuid4())
        self.base.created_at = datetime.now()
        self.base.to_dict()

    def test_name(self):
        """ test of name attribute """
        self.assertEqual(str, type(self.base.name))

    def test_id(self):
        """ test of id attribute """
        self.assertEqual(str, type(self.base.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.assertIsNotNone(self.base.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.assertIsNotNone(self.base.to_dict)

    def test__str__(self):
        """ test of __str__ """


    """Test of save"""
    def save(self):
        base = BaseModel()
        base.save()
        base.storage.new(self)

if __name__ == '__main__':
    unittest.main()
