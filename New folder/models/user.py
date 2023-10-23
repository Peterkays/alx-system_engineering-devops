#!/usr/bin/python3
"""User class definition."""
from models.base_model import BaseModel


class User(BaseModel):
    """User representation.

    Attributes:
        email (str): User email.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
