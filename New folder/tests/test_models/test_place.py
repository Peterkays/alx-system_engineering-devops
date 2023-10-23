#!/usr/bin/python3
"""Unittests for place models.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for Place class instances."""

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))



    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_city_id_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(p_lc))
        self.assertNotIn("city_id", p_lc.__dict__)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))


    def test_user_id_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(p_lc))
        self.assertNotIn("user_id", p_lc.__dict__)

    def test_name_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(p_lc))
        self.assertNotIn("name", p_lc.__dict__)

    def test_description_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(p_lc))
        self.assertNotIn("desctiption", p_lc.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(p_lc))
        self.assertNotIn("number_rooms", p_lc.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(p_lc))
        self.assertNotIn("price_by_night", p_lc.__dict__)


    def test_max_guest_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(p_lc))
        self.assertNotIn("max_guest", p_lc.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(p_lc))
        self.assertNotIn("number_bathrooms", p_lc.__dict__)

    def test_latitude_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(p_lc))
        self.assertNotIn("latitude", p_lc.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(p_lc))
        self.assertNotIn("amenity_ids", p_lc.__dict__)
    def test_two_places_different_created_at(self):
        p_lc1 = Place()
        sleep(0.05)
        p_lc2 = Place()
        self.assertLess(p_lc1.created_at, p_lc2.created_at)


    def test_two_places_unique_ids(self):
        p_lc1 = Place()
        p_lc2 = Place()
        self.assertNotEqual(p_lc1.id, p_lc2.id)

    def test_longitude_is_public_class_attribute(self):
        p_lc = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(p_lc))
        self.assertNotIn("longitude", p_lc.__dict__)



    def test_two_places_different_updated_at(self):
        p_lc1 = Place()
        sleep(0.05)
        p_lc2 = Place()
        self.assertLess(p_lc1.updated_at, p_lc2.updated_at)

    def test_str_representation(self):
        dyt_tm = datetime.today()
        dyt_tm_repr = repr(dyt_tm)
        p_lc = Place()
        p_lc.id = "123456"
        p_lc.created_at = p_lc.updated_at = dyt_tm
        p_lcstr = p_lc.__str__()
        self.assertIn("[Place] (123456)", p_lcstr)
        self.assertIn("'id': '123456'", p_lcstr)
        self.assertIn("'created_at': " + dyt_tm_repr, p_lcstr)
        self.assertIn("'updated_at': " + dyt_tm_repr, p_lcstr)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


    def test_instantiation_with_kwargs(self):
        dyt_tm = datetime.today()
        dyt_tm_iso = dyt_tm.isoformat()
        p_lc = Place(id="345", created_at=dyt_tm_iso, updated_at=dyt_tm_iso)
        self.assertEqual(p_lc.id, "345")
        self.assertEqual(p_lc.created_at, dyt_tm)
        self.assertEqual(p_lc.updated_at, dyt_tm)

    def test_args_unused(self):
        p_lc = Place(None)
        self.assertNotIn(None, p_lc.__dict__.values())


class TestPlace_save(unittest.TestCase):
    """Unittests for testing Place class save method."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_updates_file(self):
        p_lc = Place()
        p_lc.save()
        p_lcid = "Place." + p_lc.id
        with open("file.json", "r") as f:
            self.assertIn(p_lcid, f.read())


    def test_two_saves(self):
        p_lc = Place()
        sleep(0.05)
        first_updated_at = p_lc.updated_at
        p_lc.save()
        second_updated_at = p_lc.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        p_lc.save()
        self.assertLess(second_updated_at, p_lc.updated_at)

    def test_one_save(self):
        p_lc = Place()
        sleep(0.05)
        first_updated_at = p_lc.updated_at
        p_lc.save()
        self.assertLess(first_updated_at, p_lc.updated_at)

    def test_save_with_arg(self):
        p_lc = Place()
        with self.assertRaises(TypeError):
            p_lc.save(None)



class TestPlace_to_dict(unittest.TestCase):
    """Unittests for to_dict method."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        p_lc = Place()
        self.assertIn("id", p_lc.to_dict())
        self.assertIn("created_at", p_lc.to_dict())
        self.assertIn("updated_at", p_lc.to_dict())
        self.assertIn("__class__", p_lc.to_dict())

    def test_to_dict_contains_added_attributes(self):
        p_lc = Place()
        p_lc.middle_name = "Holberton"
        p_lc.my_number = 98
        self.assertEqual("Holberton", p_lc.middle_name)
        self.assertIn("my_number", p_lc.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        p_lc = Place()
        p_lc_dict = p_lc.to_dict()
        self.assertEqual(str, type(p_lc_dict["id"]))
        self.assertEqual(str, type(p_lc_dict["created_at"]))
        self.assertEqual(str, type(p_lc_dict["updated_at"]))

    def test_to_dict_output(self):
        dyt_tm = datetime.today()
        p_lc = Place()
        p_lc.id = "123456"
        p_lc.created_at = p_lc.updated_at = dyt_tm
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dyt_tm.isoformat(),
            'updated_at': dyt_tm.isoformat(),
        }
        self.assertDictEqual(p_lc.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        p_lc = Place()
        self.assertNotEqual(p_lc.to_dict(), p_lc.__dict__)

    def test_to_dict_with_arg(self):
        p_lc = Place()
        with self.assertRaises(TypeError):
            p_lc.to_dict(None)


if __name__ == "__main__":
    unittest.main()

