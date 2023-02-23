#!/usr/bin/python3
""" Unittest for Place """
import unittest
from models.base_model import BaseModel
from models.place import Place
import os


class TestPlace(unittest.TestCase):
    """ test Place """
    def test_place(self):
        """ checks place's attribute """
        self.assertEqual(self.place.city_id, "31000")
        self.assertEqual(self.place.user_id, "Charlie_6542")
        self.assertEqual(self.place.name, "chalet")
        self.assertEqual(self.place.description, "7 pièces")
        self.assertEqual(self.place.number_rooms, 4)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 10)
        self.assertEqual(self.place.price_by_night, 450)
        self.assertEqual(self.place.latitude, 43.600000)
        self.assertEqual(self.place.longitude, 1.433333)
        self.assertEqual(self.place.amenity_ids, "amenities")

if __name__ == '__main__':
    unittest.main
