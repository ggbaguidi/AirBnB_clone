#!/usr/bin/python3
"""my state class"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """
    define a state
    Attrubuts
    ---------
    name: string - empty string
    """

    name = ""
