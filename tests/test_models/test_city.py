#!/usr/bin/python3
""" Unittest for City """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ test City """
    def setUp(self):
        """ creates an instance of City """
        self.city = City()
        self.city.state_id = "31000"
        self.city.name = "Toulouse"
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
        self.assertEqual(self.city.state_id, "31000")
        self.assertEqual(self.city.name, "Toulouse")

    def test_subclass(self):
        """ checks if City is a subclass of BaseModel """
        self.assertEqual(True, issubclass(City, BaseModel))

if __name__ == '__main__':
    unittest.main
