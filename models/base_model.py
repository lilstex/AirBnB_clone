#!/usr/bin/python3

'''Defines a base model class.'''
from datetime import datetime
from uuid import uuid4

class BaseModel():
    '''A blueprint model that defines all other methods /attributes for other classes'''

    def __init__(self, id = str(uuid4()), created_at = datetime.now(), updated_at = datetime.now()):
        '''Creating an instance of a new basemodel'''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''Returns the string representation of the instantiated bject'''
        return ('[{}] ({}) {}').format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute "updated_at" with the current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__ of the instance'''
        dict = self.__dict__
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict


