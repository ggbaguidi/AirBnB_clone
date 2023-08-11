#!/usr/bin/python3
"""My city class"""

import models
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    define a city class

    Attributs
    ---------
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """

    state_id = ""
    name = ""
