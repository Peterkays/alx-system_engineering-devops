#!/usr/bin/python3
"""Review class definition."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review representation.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): Text to review.
    """

    place_id = ""
    user_id = ""
    text = ""
