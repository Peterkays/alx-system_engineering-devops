#!/usr/bin/python3
"""Unittests for user models.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for User class testing instances."""

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))


    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))


    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_two_users_different_created_at(self):
        uza1 = User()
        sleep(0.05)
        uza2 = User()
        self.assertLess(uza1.created_at, uza2.created_at)


    def test_two_users_unique_ids(self):
        uza1 = User()
        uza2 = User()
        self.assertNotEqual(uza1.id, uza2.id)

    def test_two_users_different_updated_at(self):
        uza1 = User()
        sleep(0.05)
        uza2 = User()
        self.assertLess(uza1.updated_at, uza2.updated_at)

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))


    def test_str_representation(self):
        dyt_tm = datetime.today()
        dyt_tm_repr = repr(dyt_tm)
        uza = User()
        uza.id = "123456"
        uza.created_at = uza.updated_at = dyt_tm
        uzastr = uza.__str__()
        self.assertIn("[User] (123456)", uzastr)
        self.assertIn("'id': '123456'", uzastr)
        self.assertIn("'created_at': " + dyt_tm_repr, uzastr)
        self.assertIn("'updated_at': " + dyt_tm_repr, uzastr)

    def test_args_unused(self):
        uza = User(None)
        self.assertNotIn(None, uza.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dyt_tm = datetime.today()
        dyt_tm_iso = dyt_tm.isoformat()
        uza = User(id="345", created_at=dyt_tm_iso, updated_at=dyt_tm_iso)
        self.assertEqual(uza.id, "345")
        self.assertEqual(uza.created_at, dyt_tm)
        self.assertEqual(uza.updated_at, dyt_tm)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for save method."""

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
        uza = User()
        uza.save()
        uzaid = "User." + uza.id
        with open("file.json", "r") as f:
            self.assertIn(uzaid, f.read())


    def test_two_saves(self):
        uza = User()
        sleep(0.05)
        first_updated_at = uza.updated_at
        uza.save()
        second_updated_at = uza.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        uza.save()
        self.assertLess(second_updated_at, uza.updated_at)

    def test_one_save(self):
        uza = User()
        sleep(0.05)
        first_updated_at = uza.updated_at
        uza.save()
        self.assertLess(first_updated_at, uza.updated_at)

    def test_save_with_arg(self):
        uza = User()
        with self.assertRaises(TypeError):
            uza.save(None)



class TestUser_to_dict(unittest.TestCase):
    """Unittests for to_dict method."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        uza = User()
        self.assertIn("id", uza.to_dict())
        self.assertIn("created_at", uza.to_dict())
        self.assertIn("updated_at", uza.to_dict())
        self.assertIn("__class__", uza.to_dict())

    def test_to_dict_output(self):
        dyt_tm = datetime.today()
        uza = User()
        uza.id = "123456"
        uza.created_at = uza.updated_at = dyt_tm
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dyt_tm.isoformat(),
            'updated_at': dyt_tm.isoformat(),
        }
        self.assertDictEqual(uza.to_dict(), tdict)


    def test_to_dict_datetime_attributes_are_strs(self):
        uza = User()
        uza_dict = uza.to_dict()
        self.assertEqual(str, type(uza_dict["id"]))
        self.assertEqual(str, type(uza_dict["created_at"]))
        self.assertEqual(str, type(uza_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        uza = User()
        self.assertNotEqual(uza.to_dict(), uza.__dict__)


    def test_to_dict_contains_added_attributes(self):
        uza = User()
        uza.middle_name = "Holberton"
        uza.my_number = 98
        self.assertEqual("Holberton", uza.middle_name)
        self.assertIn("my_number", uza.to_dict())

    def test_to_dict_with_arg(self):
        uza = User()
        with self.assertRaises(TypeError):
            uza.to_dict(None)


if __name__ == "__main__":
    unittest.main()

