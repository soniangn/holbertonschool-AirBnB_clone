#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models import storage
import pep8
from models.base_model import BaseModel
from models import FileStorage


class Test_Base(unittest.TestCase):
    """Base class tests"""


    def test_filestorage(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertFalse(len(storage.all()) == 0)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()