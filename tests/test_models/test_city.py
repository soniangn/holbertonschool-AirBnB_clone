#!/usr/bin/python3
"""Review"""
""" Unittest for City """
import unittest
from models.base_model import BaseModel
from models.city import City
import os


class TestCity(unittest.TestCase):
    """ test City """
    def setUp(self):
        """ creates an instance of City """
        self.city = City()
        self.city.state_id = "31000"
        self.city.name = "Toulouse"

    def test_city(self):
        """ checks city's attributes """
        self.assertEqual(self.city.state_id, "31000")
        self.assertEqual(self.city.name, "Toulouse")

if __name__ == '__main__':
    unittest.main
