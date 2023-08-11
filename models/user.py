#!/usr/bin/python3
"""My user class"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    define a User class

    Attributes
    ----------
    email: string-empty string
    password: string-empty string
    first_name: string-empty string
    last_name: string-empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
