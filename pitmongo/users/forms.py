# -*- coding: utf-8 -*-
'''
Created on Jan 6, 2016

@author: rtorres
'''
from django import forms
from pitmongo.users.models import People


class PeopleForm(forms.ModelForm):

    class Meta:
        model = People
        fields = ('name', 'surname')
