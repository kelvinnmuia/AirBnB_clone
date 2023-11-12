#!/usr/bin/python3
"""
Defines the User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    creates the User objects

    Class Attributes:
        email (str): user email
        password (str): password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
