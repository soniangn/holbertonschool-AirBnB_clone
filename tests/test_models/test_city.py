#!/usr/bin/python3
"""Review"""
""" Unittest for City """
import unittest
from models.base_model import BaseModel
from models.city import City
import os


class TestCity(unittest.TestCase):
    """ test City """
    def test_city(self):
        """ checks city's attributes """
        self.assertEqual(self.city.state_id, "31000")
        self.assertEqual(self.city.name, "Toulouse")
        self.assertEqual(True, issubclass(City, BaseModel))

if __name__ == '__main__':
    unittest.main
