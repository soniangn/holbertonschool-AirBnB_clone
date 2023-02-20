#!/usr/bin/python3
""" Module with class FileStorage """
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file """
    """ and deserializes JSON file to instances """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects = '{}.{}'.format(self.__class__.__name__, self.id)

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            for obj in self.__objects:
                json_obj = json.dumps(obj)
            f.write(json_obj)

    def reload(self):
        """ deserializes the JSON file to __objects """
        check_file = os.path.isfile(self.__file_path)
        if check_file:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                read_file = f.read()
                __objects = json.loads(read_file)
        else:
            pass
