# -*- coding: utf-8 -*-

from mongoengine import *


class Person(Document):
    name = StringField(required=True)
    surname = StringField(required=True)
