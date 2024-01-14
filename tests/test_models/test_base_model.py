#!/usr/bin/python3
"""Import necessary modules for testing"""
import unittest
import os
import pep8
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""
    @classmethod
    def setUpClass(cls):
        """Set up the test instance of BaseModel."""
        cls.testBase = BaseModel()
        cls.testBase.x = "x"
        cls.testBase.y = 100

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test instance and 'file.json' if it exists.
        """
        del cls.testBase
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_basemodel(self):
        """Test for PEP8 compliance in 'models/base_model.py'."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_check_functions(self):
        """Test for the existence of docstrings in class functions."""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attribute_basemodel(self):
        """Test for the existence of class attributes and methods."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Test the initialization of BaseModel."""
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save(self):
        """Test the 'save' method."""
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict(self):
        """Test the 'to_dict' method."""
        copy = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, 'BaseModel')
        self.assertIsInstance(copy['created_at'], str)
        self.assertIsInstance(copy['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
