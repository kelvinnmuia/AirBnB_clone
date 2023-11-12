#!/usr/bin/python3
"""
defines the FileStorage class
"""

from json import loads, dumps
from os.path import exists

class FileStorage():
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances

    Attributes:
        __file_path (str): the path to the JSON file
        __objects (dict): will help store objects by class.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary of all saved objects
        """
        return self.__objects

    def new(self, obj):
        """
         sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """
        serializes __object to the JSON file
        """
        dict_of_dicts = {}
        for key, value in self.__objects.items():
            dict_of_dicts[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(dumps(dict_of_dicts))

    def reload(self):
        """
        deserializes JSON file to __objects

        NB:
            nothing is done when JSON file (__file_path) does not exist
        """

        if exists(self.__file_path) is False:
            return

        with open(self.__file_path, 'r') as f:
            dicts = loads(f.read())

        from .known_objects import classes

        self.__objects = {}
        for id, dict in dicts.items():
            cls_name = id.split('.')[0]
            cls = classes[cls_name]
            self.__objects[id] = cls(**dict)
