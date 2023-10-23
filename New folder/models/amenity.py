#!/usr/bin/python3
"""The Amenity class definition."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of an amenity.

    Attributes:
        name (str): The name attribute of the amenity.
    """

    name = ""
