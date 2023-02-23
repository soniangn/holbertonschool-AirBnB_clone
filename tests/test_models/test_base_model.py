#!/usr/bin/python3
"""Test class base"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import os
import uuid

class TestBaseModel(unittest.TestCase):
    """Class test base"""

    def setUp(self):
        """ creates an instance of BaseModel """

    def test_name(self):
        """ test of name attribute """
        self.base = BaseModel()
        self.base.name = "BaseModel"
        self.assertEqual(str, type(self.base.name))

    def test_id(self):
        """ test of id attribute """
        self.base = BaseModel()
        self.base.id = str(uuid.uuid4())
        self.assertEqual(str, type(self.base.id))

    def test_created_at(self):
        """ test of created.at attribute """
        self.base = BaseModel()
        self.base.created_at = datetime.now()
        self.assertIsNotNone(self.base.created_at)

    def test_to_dict(self):
        """ test of to_dict method """
        self.base = BaseModel()
        self.base.to_dict()
        self.assertEqual(dict, type(self.base.to_dict()))

    def test__str__(self):
        """ test of __str__ """
        self.base = BaseModel()
        self.assertEqual(str, type(self.__str__()))

    def save(self):
        """ Test of save """
        self.base = BaseModel()
        self.base.save()
        self.assertIsNotNone(self.base.save())

if __name__ == '__main__':
    unittest.main()
