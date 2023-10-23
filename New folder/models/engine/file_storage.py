#!/usr/bin/python3
"""FileStorage class definition, 
module responsible for storage of classes and management.
"""
import json
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """Abstracted storage engine for the class.

    Attributes:
        __file_path (str): The name of file objects saved to.
        __objects (dict): The dictionary of instantiated objects to be saved in.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the contents of __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Saves objects in __objects obj with key <obj_class_name>.id"""
        objtnaim = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objtnaim, obj.id)] = obj

    def save(self):
        """Serialize contents of __objects to the JSON file __file_path."""
        obdict = FileStorage.__objects
        objectdict = {obj: obdict[obj].to_dict() for obj in obdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objectdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if file exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objectdict = json.load(f)
                for o in objectdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

