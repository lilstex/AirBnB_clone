#!/usr/bin/python3
'''A class User that inherits the Basemodel'''

from models.base_model import BaseModel

class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
