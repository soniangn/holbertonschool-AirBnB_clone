#!/usr/bin/python3
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
        obj_dict = {'id': BaseModel.id, 'created_at': BaseModel.created_at, 'updated_at': BaseModel.updated_at}
        self.assertEqual(BaseModel.__dict__, obj_dict)

    def test__str__(self):
        """ test of __str__ """
        self.assertEqual(str, f"[{BaseModel.__class__.__name__}]({BaseModel.id}){BaseModel.__dict__}")

    def test_save(self):
        """ Test of save """
        BaseModel.save()
        with open("file.json", 'r') as f:
            self.assertIn(BaseModel.id, f.read())

    if __name__ == '__main__':
        unittest.main()
