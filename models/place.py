#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """ This class, known as the Place class, establishes the attribute named 'place.'.

    Attributes:
        city_id = this is the city id.
        user_id = The User id.
        name = this is the name of the place.
        description = The description of the place.
        number_rooms = The number of rooms.
        number_bathrooms = The number of bathrooms of the place.
        max_guest =  The highest number of guests.
        price_by_night = The amount to be paid per night.
        latitude = The latitude of the place.
        longitude = The longitude of the place.
        amenity_ids = A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
