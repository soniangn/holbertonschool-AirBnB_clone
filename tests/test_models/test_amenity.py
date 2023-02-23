#!/usr/bin/python3
"""Review"""
""" Unittest for Amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test Amenity """
    def test_city(self):
        """ checks city's attributes """
        self.assertEqual(Amenity.name, "")


if __name__ == '__main__':
    unittest.main
