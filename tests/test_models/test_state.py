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
        self.assertEqual(True, issubclass(State, BaseModel))
        self.assertEqual(State.number_rooms, 0)
        self.assertEqual(State.number_bathrooms, 0)
        self.assertEqual(State.max_guest, 0)


if __name__ == '__main__':
    unittest.main
