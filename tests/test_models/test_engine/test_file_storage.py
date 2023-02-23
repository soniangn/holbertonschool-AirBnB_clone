#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models import storage
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_Base(unittest.TestCase):
    """Base class tests"""

    def safe(self):
        """  Test Dictionary """
        BaseModel.save()
        self.assertEqual(dict, type(storage.all))


if __name__ == '__main__':
    unittest.main()