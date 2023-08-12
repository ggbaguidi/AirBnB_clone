#!/usr/bin/python3
"""a base class of all model"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all others models"""

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """instanciate the class"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.update_at = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != '__class__':
                        setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())

    def __str__(self):
        """print a object"""

        class_name = self.__class__.__name__
        result_dict = self.__dict__

        return f"[{class_name}] ({self.id}) {result_dict}"

    def save(self):
        """save model"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel object."""

        dict_ = {}
        dict_["__class__"] = self.__class__.__name__
        dict_["id"] = self.id
        dict_["created_at"] = self.created_at.isoformat()
        dict_["updated_at"] = self.updated_at.isoformat()
        for key, value in self.__dict__.items():
            if key == "my_number" or key == "name":
                dict_[key] = value

        return dict_
