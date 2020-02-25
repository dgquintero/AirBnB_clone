#!/usr/bin/python3
"""FileStorage class"""
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage():
    """FileStorage class"""
    def __init__(self, *args, **kwargs):
        """Class FileStorage"""
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        j_son = {}
        for key in self.__objects:
            j_son[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(j_son, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                jsfile = json.load(f)
                for key in jsfile:
                    self.__objects[key] = classes[jsfile[key]
                                                  ["__class__"]](**jsfile[key])
        except:
            pass
