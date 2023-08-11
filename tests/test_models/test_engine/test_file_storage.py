#!usr/bin/python3
"""Put the file storage to the test"""

from models.engine.file_storage import FileStorage
import unittest
import uuid
import os


class TestStorage(unittest.TestCase):
    """
    Unittest for the storage module
    """
    def test_all(self):
        """Test the function all"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """Test the function new"""
        storage = FileStorage()
        obj = storage.all()
        pass

    def test_save(self):
        """Test the function save"""
        storage = FileStorage()
        storage.save()
        pass

    def test_reload(self):
        """Test the function reload"""
        storage = FileStorage()
        rel = storage.reload()
        self.assertIs(rel, None)
        pass


if __name__ == '__main__':
    unittest.main()
