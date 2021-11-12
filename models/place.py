#!/usr/bin/python3
<<<<<<< HEAD
'''Place Module'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''A class Place that inherits'''
=======
'''The Place class that inherits from the BaseModel'''

from models.base_model import BaseModel

class Place(BaseModel):
    '''Pass'''
>>>>>>> 214c008bf49cc94f1eea8702c544d14272b6eea5
    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
<<<<<<< HEAD
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''
=======
    latitude = float(0.0)
    amenity_ids = []
    

>>>>>>> 214c008bf49cc94f1eea8702c544d14272b6eea5
