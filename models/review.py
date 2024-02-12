#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ This class, designated as the Review class, 
    specifies attributes such as place, user,
    and review text for a given review.
    """
    
    place_id = ""
    user_id = ""
    text = ""
