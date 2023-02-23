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


    def pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        print = "Found code style errors"
        self.assertEqual(result.total_errors, 0, print)

if __name__ == '__main__':
    unittest.main()