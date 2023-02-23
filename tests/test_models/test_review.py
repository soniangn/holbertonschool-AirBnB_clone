#!/usr/bin/python3
"""Review"""
""" Unittest for Review """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test Review """
    def setUp(self):
        """ creates an instance of Review """
        self.review = Review()
        self.review.place_id = "31000"
        self.review.user_id = "Ch@arlie5433"
        self.review.text = "Great experience"

    @classmethod
    def tearDownClass(cls):
        """ delete json file at the end of tests """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_review(self):
        """ checks review's attributes """
        self.assertEqual(self.review.place_id, "31000")
        self.assertEqual(self.review.user_id, "Ch@arlie5433")
        self.assertEqual(self.review.text, "Great experience")

    def test_subclass(self):
        """ checks if Review is a subclass of BaseModel """
        self.assertEqual(True, issubclass(Review, BaseModel))

if __name__ == '__main__':
    unittest.main
