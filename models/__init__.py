#!/usr/bin/python3
"""init package file"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
