#!/usr/bin/python3
"""Review"""
""" Unittest for State """
import unittest
from models.base_model import BaseModel
from models.state import State
import os


class TestState(unittest.TestCase):
    """ test State """

    def test_state(self):
        """ checks state's attribute """
        State.name = "Haute-Garonne"
        self.assertEqual(State.name, "Haute-Garonne")

    def test_subclass(self):
        """ checks if State is a subclass of BaseModel """
        self.assertEqual(True, issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main
