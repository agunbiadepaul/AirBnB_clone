#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """ This information represent a user.

    Attributes:
        email: user email.
        password: user personal pasword.
        first_name: first name of user.
        last_name: The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
