#!/usr/bin/python3
"""
defines the BaseModel class
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    defines the common methods and attributes of the other classes
    """

    def __init__(self, *args, **kwargs):
        """
        instantiates the BaseModel class

        NB:
            when the dictionary is provided, dictionary values are used

        Common Attributes:
            id (str): to be assigned with uuid.uuid4()
            and converted to a string
            created_at: to be assigned datetime
            updated_at: assigned with datetime whenever each object is changed
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        prints string representation of class.
        Format: [<class name>] (<class id>) <class dict>
        """
        cls_name = type(self).__name__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
        return (str_rep)

    def save(self):
        """
        saves class into storage

        NB:
            used to update the public instance attribute
            'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns dictionary representation of an instance
        """
        dict_rep = {}
        time_format = datetime.isoformat
        for key in self.__dict__:
            value = self.__dict__[key]
            if key == "created_at" or key == "updated_at":
                dict_rep[key] = str(time_format(value))
            else:
                dict_rep[key] = value
        dict_rep["__class__"] = type(self).__name__
        return dict_rep
