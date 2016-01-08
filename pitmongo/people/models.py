# -*- coding: utf-8 -*-

from mongoengine import *

connect('test', host='127.0.0.1', port=27017)


class People(Document):
    name = StringField(required=True)
    surname = StringField(required=True)
    profetion = ReferenceField('Profetion')

    meta = {'indexes': [
        {'fields': ['$name', "$surname"]}
    ]}

    def clean(self):
        self.name = self.name.strip()
        self.surname = self.surname.strip()


class Profetion(Document):
    name = StringField(required=True, unique=True)

    def clean(self):
        self.name = self.name.strip().upper()
        