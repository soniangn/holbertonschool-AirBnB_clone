#!/usr/bin/python3
""" Module for User """
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ defines attributes for User """
    """ subclass of BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
