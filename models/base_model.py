#!/usr/bin/python3
""" module for BaseModel """
import uuid
from datetime import datetime

class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, id=None, created_at=None, updated_at=None, name=None, my_number=0):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = updated_at
        self.name = name
        self.my_number = my_number

    def __str__(self):
        return "[{}] ({}) {}".format(__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = dict(id=self.id, my_number=self.my_number, name=self.name, updated_at=self.updated_at, created_at=self.created_at)
        dictionary.update({'__class__': BaseModel.__name__})
        dictionary.update({'created_at': self.created_at.isoformat()})
        dictionary.update({'updated_at': self.updated_at.isoformat()})
        return dictionary