#!/usr/bin/python3
'''This file makes the models folder a python package'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()