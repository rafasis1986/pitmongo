# -*- coding: utf-8 -*-
'''
Created on Jan 7, 2016

@author: rtorres
'''
from django import forms


class PeopleForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
