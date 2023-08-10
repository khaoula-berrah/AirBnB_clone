#!/usr/bin/env python3

import uuid
import models
from datetime import datetime

"""
    base_model module.

    Module that contains, BaseModel class which all classes of inherit from.
"""


class BaseModel:
    """
        BaseModel class.
    """

    id = ""

    def __init__(self, *args, **kwargs):
        """
            BaseModel's Constructor.

            args (list): list of arguments, not not used.
            kwargs (dict): dictionary of attribute names and its values.
        """
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime.strptime(
                        kwargs[k], '%Y-%m-%dT%H:%M:%S.%f')
                elif k == '__class__':
                    continue
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def __str__(self):
        """
            function that returns a string representation of the current object.

            Return:
                (str): string representation of the current object.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
            function that updates the current object, and assign the
            update_at with the current date & time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            function that returns a dictionary containing all keys/values
            of the instance.

            Return:
                (dict): dictionary containing all keys/values of
                current instance.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return (dic)
