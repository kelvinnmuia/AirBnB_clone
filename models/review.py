#!/usr/bin/python3
"""
defines the review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review Class

    class Attributes:
        place_id (str): ID of the place with the review
        user_id (str): ID of the user leaving the review
        text (str): the review text
    """
    place_id = ""
    user_id = ""
    text = ""
