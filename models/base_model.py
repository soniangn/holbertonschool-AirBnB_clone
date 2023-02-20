#!/usr/bin/python3
"""Model from BaseModel"""
import uuid
from datetime import datetime

"""Create BaseModel"""


class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, id=None, created_at=None, updated_at=None, name=None, my_number=0):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = updated_at
        self.name = name
        self.my_number = my_number

    def __str__(self):
        """String Doc"""
        print_str = "[{}] ({}) {}"
        return print_str.format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """Save the documentation"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the Dictionnary """
        """dic = {}
        dic["id"] = self.id
        dic["created_at"] = self.created_at
        dic["my_number"] = self.my_number
        dic["updated_at"] = self.updated_at
        dic["name"] = self.name"""
        dic = dict(id=self.id, my_number=self.my_number, name=self.name, updated_at=self.updated_at, created_at=self.created_at)

        dic.update({'__class__': BaseModel.__name__})
        dic.update({'created_at': self.created_at.isoformat()})
        dic.update({'updated_at': self.updated_at.isoformat()})
        return dic
