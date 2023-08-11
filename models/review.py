#!/usr/bin/python3
"""My review class"""

import models
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
    define a Review class

    Attributs
    ---------
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
