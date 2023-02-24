#!/usr/bin/python3
"""Test class base"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import models
from datetime import datetime
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
        self.assertIn("id", BaseModel.to_dict())
        self.assertIn("created_at", BaseModel.to_dict())
        self.assertIn("updated_at", BaseModel.to_dict())
        self.assertIn("__class__", BaseModel.to_dict())

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, type(BaseModel.__str__(self)))

    def test_save(self):
        """ Test of save """
        self.assertIn(BaseModel(), models.storage.all().values())
        BaseModel.save(self)
        self.assertNotEqual(BaseModel.updated_at, BaseModel.created_at)


    if __name__ == '__main__':
        unittest.main()
