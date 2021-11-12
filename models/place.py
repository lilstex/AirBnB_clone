#!/usr/bin/python3
'''The Place class that inherits from the BaseModel'''

from models.base_model import BaseModel

class Place(BaseModel):
    '''Pass'''
    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    amenity_ids = []
    

