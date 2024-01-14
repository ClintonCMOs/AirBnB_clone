#!/usr/bin/python3
"""Unittest to test FileStorage class"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage class."""

    @classmethod
    def setUpClass(cls):
        cls.usr = User()
        cls.usr.first_name = "Andrew"
        cls.usr.last_name = "Suh"
        cls.usr.email = "andrew@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """Tear down class attributes."""
        del cls.usr

    def teardown(self):
        """Delete 'file.json' if it exists."""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_filestorage(self):
        """
        Test for PEP8 compliance in 'models/engine/file_storage.py
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all_filestorage(self):
        """
        Test the 'all' method of FileStorage.
        """
        new = FileStorage()
        instances_dic = new.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, new._FileStorage__objects)

    def test_new_filestorage(self):
        """
        Test the 'new' method of FileStorage.
        """
        altsotrage = FileStorage()
        dic = altsotrage.all()
        rev = User()
        rev.id = 69
        rev.name = "Meep"
        altsotrage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_reload_filestorage(self):
        """
        Test the 'reload' method of FileStorage.
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()

        try:
            os.remove(path)
        except:
            pass

        self.storage.save()

        with open(path, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(path)
        except:
            pass

        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
