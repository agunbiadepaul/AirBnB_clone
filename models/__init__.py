#!/usr/bin/python3
"""__init__ magic method for turning models directory into a package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
