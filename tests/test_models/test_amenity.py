#!/usr/bin/python3
"""Unittest for class Amenity"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity"""
    def setUp(self):
        """
        Create a new instance of Amenity before each test
        """
        self.a1 = Amenity()

    def tearDown(self):
        """
        Delete Amenity instance before next test
        """
        del self.a1

    def test_uniqueUUID(self):
        """
        Make sure each UUID is unique
        """
        a2 = Amenity()
        self.assertNotEqual(self.a1.id, a2.id)

    def test_id_type(self):
        """
        Make sure id is a string not uuid data type
        """
        self.assertEqual(type(self.a1.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at is datetime data type
        """
        self.assertEqual(type(self.a1.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at is datetime data type
        """
        self.assertEqual(type(self.a1.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is str data type
        """
        self.assertEqual(type(Amenity.name), str)

    def test_save(self):
        """
        Make sure save does update the updated_at attribute
        """
        old_updated_at = self.a1.updated_at
        self.a1.save()
        self.assertNotEqual(old_updated_at, self.a1.updated_at)

    def test_str(self):
        """
        Testing return of __str__
        """
        self.assertEqual(str(self.a1), "[Amenity] ({}) {}".
                         format(self.a1.id, self.a1.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns the right dictionary
        and the dict has the right attributes with the right types.
        """
        model_json = self.a1.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs to Amenity instantation
        """
        json_dict = self.a1.to_dict()
        a2 = Amenity(**json_dict)
        self.assertEqual(self.a1.id, a2.id)
        self.assertEqual(self.a1.created_at, a2.created_at)
        self.assertEqual(self.a1.updated_at, a2.updated_at)
        self.assertNotEqual(self.a1, a2)
