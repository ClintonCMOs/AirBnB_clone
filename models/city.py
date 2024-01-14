#!/usr/bin/python3
"""Import the BaseModel class from the models.base_model module"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class representing a city, inheriting from BaseModel."""
    state_id = ""
    name = ""
