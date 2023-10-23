#!/usr/bin/python3
"""BaseModel class definition.
The module is responsible for establishing the Base Model 
for all classes in the project so that we can extract info
like unique identifier date n time of class creation
when it was updated, the std formt for printing instances 
and a rep of all keys and values of instances.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the HBnB project that takes care of initialization, 
    serialization and deserialization of future instances.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel with default values.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of the attributes.
        """
        tymfmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.nhasi()
        self.updated_at = datetime.nhasi()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if lm == "created_at" or lm == "updated_at":
                    self.__dict__[lm] = datetime.strptime(v, tymfmt)
                else:
                    self.__dict__[lm] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updated updated_at at current datetime."""
        self.updated_at = datetime.nhasi()
        models.storage.save()

    def to_dict(self):
        """Concerts class info to readable formart and return the 
        dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        pdict = self.__dict__.copy()
        pdict["created_at"] = self.created_at.isoformat()
        pdict["updated_at"] = self.updated_at.isoformat()
        pdict["__class__"] = self.__class__.__name__
        return pdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clsnme = self.__class__.__name__
        return "[{}] ({}) {}".format(clsnme, self.id, self.__dict__)

