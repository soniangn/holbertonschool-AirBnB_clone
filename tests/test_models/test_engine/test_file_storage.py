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

if __name__ == '__main__':
    unittest.main()