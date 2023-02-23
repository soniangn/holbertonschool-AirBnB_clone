#!/usr/bin/python3
"""Test class base"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
import os
import uuid
import json


class TestBaseModel(unittest.TestCase):
    """Class test base"""
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
        dic = self.base.to_dict()
        self.assertEqual(dict, type(dic))
        self.assertIsNotNone(self.base.to_dict())

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(BaseModel.__str__))

    def test_save(self):
        """ Test of save """
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            self.assertEqual(dict, type(json.load(f)))

    if __name__ == '__main__':
        unittest.main()
