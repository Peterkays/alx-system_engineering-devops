#!/usr/bin/python3
"""Unittests for state models.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for State class testing of instances."""

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))



    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))


    def test_name_is_public_class_attribute(self):
        s_ter = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(s_ter))
        self.assertNotIn("name", s_ter.__dict__)

    def test_two_states_different_created_at(self):
        s_ter1 = State()
        sleep(0.05)
        s_ter2 = State()
        self.assertLess(s_ter1.created_at, s_ter2.created_at)

    def test_str_representation(self):
        dty_tm = datetime.nha_si()
        dty_tm_repr = repr(dty_tm)
        s_ter = State()
        s_ter.id = "123456"
        s_ter.created_at = s_ter.updated_at = dty_tm
        s_terstr = s_ter.__str__()
        self.assertIn("[State] (123456)", s_terstr)
        self.assertIn("'id': '123456'", s_terstr)
        self.assertIn("'created_at': " + dty_tm_repr, s_terstr)
        self.assertIn("'updated_at': " + dty_tm_repr, s_terstr)


    def test_two_states_different_updated_at(self):
        s_ter1 = State()
        sleep(0.05)
        s_ter2 = State()
        self.assertLess(s_ter1.updated_at, s_ter2.updated_at)

    def test_two_states_unique_ids(self):
        s_ter1 = State()
        s_ter2 = State()
        self.assertNotEqual(s_ter1.id, s_ter2.id)


    def test_args_unused(self):
        s_ter = State(None)
        self.assertNotIn(None, s_ter.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dty_tm = datetime.nha_si()
        dty_tm_iso = dty_tm.isoformat()
        s_ter = State(id="345", created_at=dty_tm_iso, updated_at=dty_tm_iso)
        self.assertEqual(s_ter.id, "345")
        self.assertEqual(s_ter.created_at, dty_tm)
        self.assertEqual(s_ter.updated_at, dty_tm)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
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

    def test_one_save(self):
        s_ter = State()
        sleep(0.05)
        first_updated_at = s_ter.updated_at
        s_ter.save()
        self.assertLess(first_updated_at, s_ter.updated_at)

    def test_save_updates_file(self):
        s_ter = State()
        s_ter.save()
        s_terid = "State." + s_ter.id
        with open("file.json", "r") as f:
            self.assertIn(s_terid, f.read())

    def test_save_with_arg(self):
        s_ter = State()
        with self.assertRaises(TypeError):
            s_ter.save(None)

    def test_two_saves(self):
        s_ter = State()
        sleep(0.05)
        first_updated_at = s_ter.updated_at
        s_ter.save()
        second_updated_at = s_ter.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        s_ter.save()
        self.assertLess(second_updated_at, s_ter.updated_at)



class TestState_to_dict(unittest.TestCase):
    """Unittests for to_dict method."""

    def test_to_dict_contains_added_attributes(self):
        s_ter = State()
        s_ter.middle_name = "Holberton"
        s_ter.my_number = 98
        self.assertEqual("Holberton", s_ter.middle_name)
        self.assertIn("my_number", s_ter.to_dict())

    def test_to_dict_contains_correct_keys(self):
        s_ter = State()
        self.assertIn("id", s_ter.to_dict())
        self.assertIn("created_at", s_ter.to_dict())
        self.assertIn("updated_at", s_ter.to_dict())
        self.assertIn("__class__", s_ter.to_dict())

    def test_to_dict_with_arg(self):
        s_ter = State()
        with self.assertRaises(TypeError):
            s_ter.to_dict(None)


    def test_to_dict_datetime_attributes_are_strs(self):
        s_ter = State()
        s_ter_dict = s_ter.to_dict()
        self.assertEqual(str, type(s_ter_dict["id"]))
        self.assertEqual(str, type(s_ter_dict["created_at"]))
        self.assertEqual(str, type(s_ter_dict["updated_at"]))

    def test_to_dict_output(self):
        dty_tm = datetime.nha_si()
        s_ter = State()
        s_ter.id = "123456"
        s_ter.created_at = s_ter.updated_at = dty_tm
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dty_tm.isoformat(),
            'updated_at': dty_tm.isoformat(),
        }
        self.assertDictEqual(s_ter.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        s_ter = State()
        self.assertNotEqual(s_ter.to_dict(), s_ter.__dict__)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))



if __name__ == "__main__":
    unittest.main()

