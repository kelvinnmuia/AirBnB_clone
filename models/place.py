#!/usr/bin/python3
"""
defines the place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    The place Class

    class Attributes:
        city_id (str): ID of the city that a place belongs to
        user_id (str): ID of the user that owns the place
        name (str): name of the place
        description (str): the description of the place
        number_rooms (int): the number of available rooms
        number_bathrooms (int): the number of available bathrooms
        max_guest (int): the maximum number of guests allowed
        price_by_night (int): price by night
        latitude (float): latitude coordinate
        longitude (float): longitude coordinate
        amenity_ids (list of str): the list of amenities provided
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latutude = 0.0
    longitude = 0.0
    amenity_ids = []
