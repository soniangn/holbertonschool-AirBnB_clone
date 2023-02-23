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
        self.assertEqual(State.name, '')

if __name__ == '__main__':
    unittest.main
