#!/usr/bin/python3
"""Base class defining common attributes and methods for other classes."""
import uuid
from datetime import datetime
import models

class BaseModel:
    """A base_model class"""
    def __init__(self, *args, **kwargs):
        """Initialize an instance of the class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Return a string representation of the object."""
        return self.__str__()

    def save(self):
        """Save the current instance and update the timestamp."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        copy = dict(self.__dict__)
        copy['__class__'] = str(self.__class__.__name__)
        copy['created_at'] = self.created_at.isoformat()
        copy['updated_at'] = self.updated_at.isoformat()
        return copy
