# -*- coding: utf-8 -*-
'''
Created on Jan 7, 2016

@author: rtorres
'''
from django import forms
from pitmongo.people.models import Profetion


class PeopleForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    profetion = forms.ChoiceField(widget=forms.Select())

    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        CHOICE = ((item.pk, item.name) for item in Profetion.objects().order_by('name'))
        self.fields['profetion'].choices = CHOICE


class ProfetionForm(forms.Form):
    name = forms.CharField()
