#!/usr/bin/python3
"""Unittests for review models.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for Review class testing instances."""

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))


    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_two_reviews_unique_ids(self):
        rivw1 = Review()
        rivw2 = Review()
        self.assertNotEqual(rivw1.id, rivw2.id)


    def test_user_id_is_public_class_attribute(self):
        rivw = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rivw))
        self.assertNotIn("user_id", rivw.__dict__)

    def test_place_id_is_public_class_attribute(self):
        rivw = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rivw))
        self.assertNotIn("place_id", rivw.__dict__)

    def test_text_is_public_class_attribute(self):
        rivw = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rivw))
        self.assertNotIn("text", rivw.__dict__)


    def test_two_reviews_different_created_at(self):
        rivw1 = Review()
        sleep(0.05)
        rivw2 = Review()
        self.assertLess(rivw1.created_at, rivw2.created_at)

    def test_two_reviews_different_updated_at(self):
        rivw1 = Review()
        sleep(0.05)
        rivw2 = Review()
        self.assertLess(rivw1.updated_at, rivw2.updated_at)

    def test_str_representation(self):
        dty_tm = datetime.today()
        dty_tm_repr = repr(dty_tm)
        rivw = Review()
        rivw.id = "123456"
        rivw.created_at = rivw.updated_at = dty_tm
        rivwstr = rivw.__str__()
        self.assertIn("[Review] (123456)", rivwstr)
        self.assertIn("'id': '123456'", rivwstr)
        self.assertIn("'created_at': " + dty_tm_repr, rivwstr)
        self.assertIn("'updated_at': " + dty_tm_repr, rivwstr)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


    def test_instantiation_with_kwargs(self):
        dty_tm = datetime.today()
        dty_tm_iso = dty_tm.isoformat()
        rivw = Review(id="345", created_at=dty_tm_iso, updated_at=dty_tm_iso)
        self.assertEqual(rivw.id, "345")
        self.assertEqual(rivw.created_at, dty_tm)
        self.assertEqual(rivw.updated_at, dty_tm)

    def test_args_unused(self):
        rivw = Review(None)
        self.assertNotIn(None, rivw.__dict__.values())


class TestReview_save(unittest.TestCase):
    """Unittests for the save method."""

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
        rivw = Review()
        rivw.save()
        rivwid = "Review." + rivw.id
        with open("file.json", "r") as f:
            self.assertIn(rivwid, f.read())


    def test_two_saves(self):
        rivw = Review()
        sleep(0.05)
        first_updated_at = rivw.updated_at
        rivw.save()
        second_updated_at = rivw.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rivw.save()
        self.assertLess(second_updated_at, rivw.updated_at)

    def test_one_save(self):
        rivw = Review()
        sleep(0.05)
        first_updated_at = rivw.updated_at
        rivw.save()
        self.assertLess(first_updated_at, rivw.updated_at)

    def test_save_with_arg(self):
        rivw = Review()
        with self.assertRaises(TypeError):
            rivw.save(None)




class TestReview_to_dict(unittest.TestCase):
    """Unittests for to_dict method."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        rivw = Review()
        self.assertIn("id", rivw.to_dict())
        self.assertIn("created_at", rivw.to_dict())
        self.assertIn("updated_at", rivw.to_dict())
        self.assertIn("__class__", rivw.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rivw = Review()
        rivw.middle_name = "Holberton"
        rivw.my_number = 98
        self.assertEqual("Holberton", rivw.middle_name)
        self.assertIn("my_number", rivw.to_dict())

    def test_to_dict_with_arg(self):
        rivw = Review()
        with self.assertRaises(TypeError):
            rivw.to_dict(None)


    def test_to_dict_output(self):
        dty_tm = datetime.today()
        rivw = Review()
        rivw.id = "123456"
        rivw.created_at = rivw.updated_at = dty_tm
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dty_tm.isoformat(),
            'updated_at': dty_tm.isoformat(),
        }
        self.assertDictEqual(rivw.to_dict(), tdict)

    def test_to_dict_datetime_attributes_are_strs(self):
        rivw = Review()
        rivw_dict = rivw.to_dict()
        self.assertEqual(str, type(rivw_dict["id"]))
        self.assertEqual(str, type(rivw_dict["created_at"]))
        self.assertEqual(str, type(rivw_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        rivw = Review()
        self.assertNotEqual(rivw.to_dict(), rivw.__dict__)



if __name__ == "__main__":
    unittest.main()

