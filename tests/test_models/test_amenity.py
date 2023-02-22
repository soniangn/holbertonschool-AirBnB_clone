#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test Amenity """
    def setUp(self):
        """ creates an instance of Amenity """
        self.amenity = Amenity()
        self.amenity.name = "air-conditioning"
"""
    @classmethod
    def tearDownClass(cls):
        """ delete json file at the end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass
"""
    def test_city(self):
        """ checks city's attributes """
        self.assertEqual(self.amenity.name, "air-conditioning")
    
    def test_subclass(self):
        """ checks if Amenity is a subclass of BaseModel """
        self.assertEqual(True, issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main