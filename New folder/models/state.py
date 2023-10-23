#!/usr/bin/python3
"""State class definition."""
from models.base_model import BaseModel


class State(BaseModel):
    """State representation.

    Attributes:
        name (str): State name.
    """

    name = ""
