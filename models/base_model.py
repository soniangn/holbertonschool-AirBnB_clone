#!/usr/bin/python3
"""Model from BaseModel"""
import uuid
from datetime import datetime

"""Create BaseModel"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format)
                if key == 'my_number':
                    self.my_number = value
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, format)
                if key == 'name':
                    self.name = value
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String Doc"""
        print_str = "[{}] ({}) {}"
        return print_str.format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """Save the documentation"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the Dictionnary """
        dic = {}
        dic["id"] = self.id
        dic["created_at"] = self.created_at
        dic["my_numbers"] = self.my_number
        dic["updated_at"] = self.updated_at
        dic["name"] = self.name

        dic.update({'__class__': BaseModel.__name__})
        dic.update({'created_at': self.created_at.isoformat()})
        dic.update({'updated_at': self.updated_at.isoformat()})
        return dic
