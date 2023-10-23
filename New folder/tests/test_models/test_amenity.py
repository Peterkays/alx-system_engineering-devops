#!/usr/bin/python3
"""This module contains unittests for amenities.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """This class contains Unittests for testing instantiation."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())


    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))


    def test_name_is_public_class_attribute(self):
        amety_ = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amety_.__dict__)

    def test_two_amenities_different_updated_at(self):
        amety_1 = Amenity()
        sleep(0.05)
        amety_2 = Amenity()
        self.assertLess(amety_1.updated_at, amety_2.updated_at)

    def test_two_amenities_unique_ids(self):
        amety_1 = Amenity()
        amety_2 = Amenity()
        self.assertNotEqual(amety_1.id, amety_2.id)

    def test_two_amenities_different_created_at(self):
        amety_1 = Amenity()
        sleep(0.05)
        amety_2 = Amenity()
        self.assertLess(amety_1.created_at, amety_2.created_at)

    

    def test_str_representation(self):
        dyt_tm = datetime.today()
        dyt_tm_repr = repr(dyt_tm)
        amety_ = Amenity()
        amety_.id = "123456"
        amety_.created_at = amety_.updated_at = dyt_tm
        amstr = amety_.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dyt_tm_repr, amstr)
        self.assertIn("'updated_at': " + dyt_tm_repr, amstr)

    def test_args_unused(self):
        amety_ = Amenity(None)
        self.assertNotIn(None, amety_.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_kwargs(self):
        """instantiation using the kwargs method"""
        dyt_tm = datetime.today()
        dyt_tm_iso = dyt_tm.isoformat()
        amety_ = Amenity(id="345", created_at=dyt_tm_iso, updated_at=dyt_tm_iso)
        self.assertEqual(amety_.id, "345")
        self.assertEqual(amety_.created_at, dyt_tm)
        self.assertEqual(amety_.updated_at, dyt_tm)



class TestAmenity_save(unittest.TestCase):
    """Unittests for testing the save method."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_save_with_arg(self):
        amety_ = Amenity()
        with self.assertRaises(TypeError):
            amety_.save(None)

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amety_ = Amenity()
        sleep(0.05)
        first_updated_at = amety_.updated_at
        amety_.save()
        self.assertLess(first_updated_at, amety_.updated_at)

    def test_two_saves(self):
        amety_ = Amenity()
        sleep(0.05)
        first_updated_at = amety_.updated_at
        amety_.save()
        second_updated_at = amety_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amety_.save()
        self.assertLess(second_updated_at, amety_.updated_at)

    

    def test_save_updates_file(self):
        amety_ = Amenity()
        amety_.save()
        amid = "Amenity." + amety_.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for to_dict method."""

    
    def test_to_dict_datetime_attributes_are_strs(self):
        amety_ = Amenity()
        amety__dict = amety_.to_dict()
        self.assertEqual(str, type(amety__dict["id"]))
        self.assertEqual(str, type(amety__dict["created_at"]))
        self.assertEqual(str, type(amety__dict["updated_at"]))

    def test_to_dict_contains_correct_keys(self):
        amety_ = Amenity()
        self.assertIn("id", amety_.to_dict())
        self.assertIn("created_at", amety_.to_dict())
        self.assertIn("updated_at", amety_.to_dict())
        self.assertIn("__class__", amety_.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amety_ = Amenity()
        amety_.middle_name = "Holberton"
        amety_.my_number = 98
        self.assertEqual("Holberton", amety_.middle_name)
        self.assertIn("my_number", amety_.to_dict())

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_output(self):
        dyt_tm = datetime.today()
        amety_ = Amenity()
        amety_.id = "123456"
        amety_.created_at = amety_.updated_at = dyt_tm
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dyt_tm.isoformat(),
            'updated_at': dyt_tm.isoformat(),
        }
        self.assertDictEqual(amety_.to_dict(), tdict)

    def test_to_dict_with_arg(self):
        amety_ = Amenity()
        with self.assertRaises(TypeError):
            amety_.to_dict(None)
    def test_contrast_to_dict_dunder_dict(self):
        amety_ = Amenity()
        self.assertNotEqual(amety_.to_dict(), amety_.__dict__)


if __name__ == "__main__":
    unittest.main()

