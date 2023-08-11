#!/usr/bin/python3
"""Test suit for the models"""

import unittest
import os
import re
import uuid
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This is just an example TestCase"""
    @classmethod
    def setUpCalss(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Eeeeeh"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("objects.json")
        except Exception:
            pass

    def test_save(self):
        """First test baby"""
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_to_dict(self):
        """This tests the to_dict method"""
        pass

    def test_id(self):
        """This tests the id"""
        pass

    def test_created_at(self):
        """This tests the format of time"""
        pass

    def test___str__(self):
        """This is to test __str__"""
        pass

    def test___init__(self):
        """This is to test __init__"""
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))


if __name__ == '__main__':
    """not sure"""
    unittest.main()
