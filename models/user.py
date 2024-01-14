#!/usr/bin/python3
"""Import the BaseModel class from the models.base_model module"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class User inherited from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
