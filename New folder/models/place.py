#!/usr/bin/python3
"""The Place class definition."""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place representation.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): Place name.
        description (str): Place description.
        number_rooms (int): Number of rooms found in the place.
        number_bathrooms (int): Bathrooms number in the place.
        max_guest (int): Max number of guests at the place.
        price_by_night (int): Night price of the place.
        latitude (float): Place latitude.
        longitude (float): Place longitude.
        amenity_ids (list): List of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
