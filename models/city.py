#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel
import models

class City(BaseModel):
    """ This class, known as the city class, establishes the attribute 'city.'

        state_id = The state id.
        name = city name.
    """

    state_id = ""
    name = ""
