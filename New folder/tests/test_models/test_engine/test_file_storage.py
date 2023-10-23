#!/usr/bin/python3
"""Unittests for engine/file_storage model

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing FileStorage class instances."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)



class TestFileStorage_methods(unittest.TestCase):
    """Unittests for methods."""

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
        FileStorage._FileStorage__objects = {}

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bs_mdl = BaseModel()
        uza = User()
        s_ter = State()
        p_lc = Place()
        cty = City()
        amety_ = Amenity()
        rivw = Review()
        models.storage.new(bs_mdl)
        models.storage.new(uza)
        models.storage.new(s_ter)
        models.storage.new(p_lc)
        models.storage.new(cty)
        models.storage.new(amety_)
        models.storage.new(rivw)
        self.assertIn("BaseModel." + bs_mdl.id, models.storage.all().keys())
        self.assertIn(bs_mdl, models.storage.all().values())
        self.assertIn("User." + uza.id, models.storage.all().keys())
        self.assertIn(uza, models.storage.all().values())
        self.assertIn("State." + s_ter.id, models.storage.all().keys())
        self.assertIn(s_ter, models.storage.all().values())
        self.assertIn("Place." + p_lc.id, models.storage.all().keys())
        self.assertIn(p_lc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amety_.id, models.storage.all().keys())
        self.assertIn(amety_, models.storage.all().values())
        self.assertIn("Review." + rivw.id, models.storage.all().keys())
        self.assertIn(rivw, models.storage.all().values())

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))


    def test_save(self):
        bs_mdl = BaseModel()
        uza = User()
        s_ter = State()
        p_lc = Place()
        cty = City()
        amety_ = Amenity()
        rivw = Review()
        models.storage.new(bs_mdl)
        models.storage.new(uza)
        models.storage.new(s_ter)
        models.storage.new(p_lc)
        models.storage.new(cty)
        models.storage.new(amety_)
        models.storage.new(rivw)
        models.storage.save()
        sve_txt = ""
        with open("file.json", "r") as f:
            sve_txt = f.read()
            self.assertIn("BaseModel." + bs_mdl.id, sve_txt)
            self.assertIn("User." + uza.id, sve_txt)
            self.assertIn("State." + s_ter.id, sve_txt)
            self.assertIn("Place." + p_lc.id, sve_txt)
            self.assertIn("City." + cty.id, sve_txt)
            self.assertIn("Amenity." + amety_.id, sve_txt)
            self.assertIn("Review." + rivw.id, sve_txt)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bs_mdl = BaseModel()
        uza = User()
        s_ter = State()
        p_lc = Place()
        cty = City()
        amety_ = Amenity()
        rivw = Review()
        models.storage.new(bs_mdl)
        models.storage.new(uza)
        models.storage.new(s_ter)
        models.storage.new(p_lc)
        models.storage.new(cty)
        models.storage.new(amety_)
        models.storage.new(rivw)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bs_mdl.id, objs)
        self.assertIn("User." + uza.id, objs)
        self.assertIn("State." + s_ter.id, objs)
        self.assertIn("Place." + p_lc.id, objs)
        self.assertIn("City." + cty.id, objs)
        self.assertIn("Amenity." + amety_.id, objs)
        self.assertIn("Review." + rivw.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

