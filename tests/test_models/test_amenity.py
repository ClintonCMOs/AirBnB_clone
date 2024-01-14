#!/usr/bin/python3
"""Import necessary modules for testing"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Set up for testing."""
        cls.lord = Amenity()
        cls.lord.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """Tear down after testing."""
        del cls.lord

    def tearDown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_Amen(self):
        """Test for PEP8 compliance in 'models/amenity.py'."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_Amen(self):
        """Test for the existence of docstrings."""
        self.assertIsNotNone(self.lord.__doc__)

    def test_attr_Amen(self):
        """Check if Amenity class has required attributes."""
        self.assertTrue('id' in self.lord.__dict__)
        self.assertTrue('created_at' in self.lord.__dict__)
        self.assertTrue('updated_at' in self.lord.__dict__)
        self.assertTrue('name' in self.lord.__dict__)

    def test_inheritance_Amen(self):
        """Test if Amenity class inherits from BaseModel."""
        self.assertTrue(issubclass(self.lord.__class__, BaseModel), True)

    def test_attrtype_Amen(self):
        """Test attribute types in the Amenity instance."""
        self.assertEqual(type(self.lord.name), str)

    def test_save(self):
        """Test the save function."""
        self.lord.save()
        self.assertNotEqual(self.lord.created_at, self.lord.updated_at)

    def test_to_dict(self):
        """Test if the 'to_dict' function works."""
        self.assertEqual('to_dict' in dir(self.lord), True)

if __name__ == "__main__":
    unittest.main()
