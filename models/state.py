#!/usr/bin/python3
""" Defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ This class, known as the State class, establishes the attribute named 'name'.

    name (str): The name of the state.
    """
    name = ""

    def __init(self, *arg, **kwarg):
        """initialises the state class"""
        super().__init__(self, *arg, **kwarg)
