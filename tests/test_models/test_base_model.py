#!/usr/bin/python3
"""Test class base"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models.engine.file_storage
import os
import uuid


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
        self.base = BaseModel()
        self.assertEqual(str, type(self.__str__()))

    def save(self):
        """ Test of save """
        base = BaseModel()
        base.save()
        self.assertEqual(dict, type(storage.all))

    if __name__ == '__main__':
        unittest.main()
