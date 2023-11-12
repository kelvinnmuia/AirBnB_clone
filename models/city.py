#!/usr/bin/python3
"""
defines the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The City Class

    class Attributes:
        name (str): name of city
        state_id (str): State's id where the city is located
    """
    name = ""
    state_id = ""
