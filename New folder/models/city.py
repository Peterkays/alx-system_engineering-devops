#!/usr/bin/python3
"""The City class definition."""
from models.base_model import BaseModel


class City(BaseModel):
    """A city representation.

    Attributes:
        state_id (str): State id.
        name (str): The city name.
    """

    state_id = ""
    name = ""
