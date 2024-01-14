#!/usr/bin/python3
"""Import the BaseModel class from the models.base_model module"""
from models.base_model import BaseModel

class State(BaseModel):
    """A class representing a state, inheriting from BaseModel."""
    name = ""
