#!/usr/bin/python3
'''User module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A class User that inherits'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
