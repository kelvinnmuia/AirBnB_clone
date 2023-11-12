#!/usr/bin/python3
"""
known classes
"""

from ..base_model import BaseModel
from ..user import User
from ..city import City
from ..state import State
from ..place import Place
from ..review import Review
from ..amenity import Amenity

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity,
}

console_methods = ["all", "count", "show", "destroy", "update"]
