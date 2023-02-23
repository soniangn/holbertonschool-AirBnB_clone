#!/usr/bin/python3
"""Review"""
""" Unittest for City """
import unittest
from models.base_model import BaseModel
from models.city import City
import os


class TestCity(unittest.TestCase):

    def test_city(self):
        """ creates an instance of City """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

if __name__ == '__main__':
    unittest.main
