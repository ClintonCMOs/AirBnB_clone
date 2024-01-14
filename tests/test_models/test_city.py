#!/usr/bin/python3
"""Import necessary modules for testing"""
import unittest
import pep8
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    @classmethod
    def setUp(cls):
        """Create a test instance of City."""
        cls.testCity = City()
        cls.testCity.name = "test"
        cls.testCity.state_id = "T"

    @classmethod
    def tearDown(cls):
        """Delete the test instance and 'file.json' if it exists."""
        del cls.testCity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_city(self):
        """Test for PEP8 compliance in 'models/city.py'."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings_city(self):
        """Test for the existence of docstrings."""
        self.assertTrue(len(City.__doc__) > 0)
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables_city(self):
        """Test initialization and class variables."""
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(issubclass(type(self.testCity), BaseModel))
        self.assertTrue(self.testCity.name == "test")
        self.assertTrue(self.testCity.state_id == "T")
        self.assertIsNotNone(self.testCity.id)
        self.assertIsNotNone(self.testCity.updated_at)
        self.assertIsNotNone(self.testCity.created_at)

    def test_save_city(self):
        """Test the 'save' method."""
        self.testCity.save()
        self.assertTrue(self.testCity.updated_at != self.testCity.created_at)

if __name__ == '__main__':
    unittest.main()
