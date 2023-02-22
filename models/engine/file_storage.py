#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
""" Module with class FileStorage """


class FileStorage:
    """ serializes instances to a JSON file """
    """ and deserializes JSON file to instances """
    __file_path = 'file.json'
    __objects = {}

    classes = {'BaseModel': BaseModel,
               'User': User, 
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity, 
               'Review': Review}

    def all(self):
        """ return the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
