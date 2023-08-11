#!/usr/bin/python3
"""Test User"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest


class Testuser(unittest.TestCase):
    """
    Unittests for the User class.
    """

    def test_user(self):
        """Test that we conform to PEP8."""
        user = User()
        self.assertIsNotNone(user)
