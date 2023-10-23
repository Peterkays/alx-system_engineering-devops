#!/usr/bin/python3
"""Unittests for base models.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for instantiation of BaseModel class."""

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))


    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_two_models_different_created_at(self):
        bs_mdl1 = BaseModel()
        sleep(0.05)
        bs_mdl2 = BaseModel()
        self.assertLess(bs_mdl1.created_at, bs_mdl2.created_at)


    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_models_unique_ids(self):
        bs_mdl1 = BaseModel()
        bs_mdl2 = BaseModel()
        self.assertNotEqual(bs_mdl1.id, bs_mdl2.id)

    def test_str_representation(self):
        dyt_tm = datetime.today()
        dyt_tm_repr = repr(dyt_tm)
        bs_mdl = BaseModel()
        bs_mdl.id = "123456"
        bs_mdl.created_at = bs_mdl.updated_at = dyt_tm
        bs_mdlstr = bs_mdl.__str__()
        self.assertIn("[BaseModel] (123456)", bs_mdlstr)
        self.assertIn("'id': '123456'", bs_mdlstr)
        self.assertIn("'created_at': " + dyt_tm_repr, bs_mdlstr)
        self.assertIn("'updated_at': " + dyt_tm_repr, bs_mdlstr)


    def test_two_models_different_updated_at(self):
        bs_mdl1 = BaseModel()
        sleep(0.05)
        bs_mdl2 = BaseModel()
        self.assertLess(bs_mdl1.updated_at, bs_mdl2.updated_at)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


    def test_args_unused(self):
        bs_mdl = BaseModel(None)
        self.assertNotIn(None, bs_mdl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dyt_tm = datetime.today()
        dyt_tm_iso = dyt_tm.isoformat()
        bs_mdl = BaseModel(id="345", created_at=dyt_tm_iso, updated_at=dyt_tm_iso)
        self.assertEqual(bs_mdl.id, "345")
        self.assertEqual(bs_mdl.created_at, dyt_tm)
        self.assertEqual(bs_mdl.updated_at, dyt_tm)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_instantiation_with_args_and_kwargs(self):
        dyt_tm = datetime.today()
        dyt_tm_iso = dyt_tm.isoformat()
        bs_mdl = BaseModel("12", id="345", created_at=dyt_tm_iso, updated_at=dyt_tm_iso)
        self.assertEqual(bs_mdl.id, "345")
        self.assertEqual(bs_mdl.created_at, dyt_tm)
        self.assertEqual(bs_mdl.updated_at, dyt_tm)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for save method for BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
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
        bs_mdl = BaseModel()
        sleep(0.05)
        first_updated_at = bs_mdl.updated_at
        bs_mdl.save()
        self.assertLess(first_updated_at, bs_mdl.updated_at)

    def test_two_saves(self):
        bs_mdl = BaseModel()
        sleep(0.05)
        first_updated_at = bs_mdl.updated_at
        bs_mdl.save()
        second_updated_at = bs_mdl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bs_mdl.save()
        self.assertLess(second_updated_at, bs_mdl.updated_at)

    def test_save_with_arg(self):
        bs_mdl = BaseModel()
        with self.assertRaises(TypeError):
            bs_mdl.save(None)

    def test_save_updates_file(self):
        bs_mdl = BaseModel()
        bs_mdl.save()
        bs_mdlid = "BaseModel." + bs_mdl.id
        with open("file.json", "r") as f:
            self.assertIn(bs_mdlid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for to_dict."""

    def test_to_dict_contains_correct_keys(self):
        bs_mdl = BaseModel()
        self.assertIn("id", bs_mdl.to_dict())
        self.assertIn("created_at", bs_mdl.to_dict())
        self.assertIn("updated_at", bs_mdl.to_dict())
        self.assertIn("__class__", bs_mdl.to_dict())
def test_to_dict_type(self):
        bs_mdl = BaseModel()
        self.assertTrue(dict, type(bs_mdl.to_dict()))

    def test_contrast_to_dict_dunder_dict(self):
        bs_mdl = BaseModel()
        self.assertNotEqual(bs_mdl.to_dict(), bs_mdl.__dict__)

    def test_to_dict_contains_added_attributes(self):
        bs_mdl = BaseModel()
        bs_mdl.name = "Holberton"
        bs_mdl.my_number = 98
        self.assertIn("name", bs_mdl.to_dict())
        self.assertIn("my_number", bs_mdl.to_dict())

    def test_to_dict_with_arg(self):
        bs_mdl = BaseModel()
        with self.assertRaises(TypeError):
            bs_mdl.to_dict(None)

    def test_to_dict_output(self):
        dyt_tm = datetime.today()
        bs_mdl = BaseModel()
        bs_mdl.id = "123456"
        bs_mdl.created_at = bs_mdl.updated_at = dyt_tm
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dyt_tm.isoformat(),
            'updated_at': dyt_tm.isoformat()
        }
        self.assertDictEqual(bs_mdl.to_dict(), tdict)

    def test_to_dict_datetime_attributes_are_strs(self):
        bs_mdl = BaseModel()
        bs_mdl_dict = bs_mdl.to_dict()
        self.assertEqual(str, type(bs_mdl_dict["created_at"]))
        self.assertEqual(str, type(bs_mdl_dict["updated_at"]))

    


if __name__ == "__main__":
    unittest.main()

