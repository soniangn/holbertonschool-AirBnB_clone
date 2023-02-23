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

    def test_1(self):
        """  Test Dictionary """
        BaseModel.save()
        self.assertEqual(dict, type(storage.all))

    def test_reload(self):
        """Test of reload()"""
        with self.assertRaises(TypeError):
            FileStorage.reload(None)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()