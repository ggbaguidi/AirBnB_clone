#!/usr/bin/python3
"""a class file storage"""

import os
import json

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """define file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """alll objects"""

        return self.__objects

    def new(self, obj):
        """ sets objects"""

        self.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        """serialization"""

        dict_ = {}

        for key_obj in self.__objects.keys():
            dict_[key_obj] = self.__objects[key_obj].to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dict_))

    def reload(self):
        """deserialization"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                dict_ = json.loads(f.read())
            for key, obj in dict_.items():
                self.__objects[key] = eval(obj["__class__"])(**obj)
