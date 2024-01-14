#!/usr/bin/python3
"""Import necessary modules for testing"""
import unittest
from io import StringIO
from unittest.mock import patch
import pep8
import os
import console
import tests
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """Tests for the console, including 'quit' and 'empty' commands."""

    @classmethod
    def setUpClass(cls):
        """Set up the console class for testing."""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """Tear down the console class."""
        del cls.consol

    def tearDown(self):
        """Delete the 'file.json' file if it exists."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Test for PEP8 compliance in the 'console.py' file."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """Check for docstrings in console commands."""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test for handling an empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("test")
            self.assertEqual("*** Unknown syntax: test\n", f.getvalue())

    def test_quit(self):
        """Test the 'quit' command functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())
