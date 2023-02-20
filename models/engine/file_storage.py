#!/usr/bin/python3
""" Module with class FileStorage """
import json
import os.path


class FileStorage:
    """ serializes instances to a JSON file """
    """ and deserializes JSON file to instances """
    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects

    @property
    def all(self):
        """ return the dictionary __objects """
        return self.__objects

    @objects.setter
    def new(self, obj): 
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects = '{}.{}'.format(self.__class__.__name__, self.id)

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding=utf-8) as f:
            for obj in self.__objects: 
                json_obj = json.dumps(obj)
            f.write(json_obj)

    def reload(self):
        """ deserializes the JSON file to __objects """
        check_file = os.path.isfile(self.__file_path)
        if check_file:
            with open(self.__file_path, "r", encoding=utf-8) as f:
                read_file = f.read()
                __objects = json.loads(read_file)
        else:
            pass
