# -*- coding: utf-8 -*-

from mongoengine import *


class People(Document):
    name = StringField(required=True)
    surname = StringField(required=True)
