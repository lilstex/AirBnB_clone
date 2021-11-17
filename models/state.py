#!/usr/bin/python3
'''The state class that inherits from the BaseModel'''

from models.base_model import BaseModel

class State(BaseModel):
    '''This class takes care of all the state related matters of the application'''
    name = ''
    count = 0

