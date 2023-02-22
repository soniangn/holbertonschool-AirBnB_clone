#!/usr/bin/python3
""" Module for Review """
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """ defines attributes for Review """
    """ subclass of BaseModel """
    place_id = ""
    user_id = ""
    text = ""
