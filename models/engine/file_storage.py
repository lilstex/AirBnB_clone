#!/usr/bin/python3
from json import dump, load
from models.base_model import BaseModel

class FileStorage():
    '''Serializes instances to a JSON file and deserializes JSON file to instances'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''Saves in __objects dictionary, the object with key <obj class name>.id'''
        key = '{}.{}'.format(obj.__class__.__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serializes and saves __objects to the JSON file (path: __file_path)'''
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file_object:
            dump(dict, file_object)

    def reload(self):
        '''Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists'''
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file_object:
                dict = load(file_object)
        except: 
            return
        