#!/usr/bin/python3
""" Unittest for State """
import unittest
from models.base_model import BaseModel
from models.state import State
import os


class TestState(unittest.TestCase):
    """ test State """
    def setUp(self):
        """ creates an instance of State with attributes """
        self.state = State()
        self.state.name = "Haute-Garonne"

    @classmethod
    def tearDownClass(cls):
        """ delete json file at the end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_user(self):
        """ checks state's attribute """
        self.assertEqual(self.state.name, "Haute-Garonne")

    def test_subclass(self):
        """ checks if State is a subclass of BaseModel """
        self.assertEqual(True, issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main