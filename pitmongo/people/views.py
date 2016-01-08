# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView
from mongoengine.connection import connect

from pitmongo.people.forms import PeopleForm
from pitmongo.people.models import People


LIST_PEOPLE = 'people:list'
OBJ_NAME = 'object_name'
OBJ_TEMP = 'object_template'
PEOPLE_DELETE = ''
PEOPLE_DETAIL = 'people/people_detail.html'
PEOPLE_FORM = 'people/people_form.html'
PEOPLE_LIST = 'people/people_list.html'
PEOPLE_NAME = 'people'
PEOPLE_TEMP = PEOPLE_NAME


connect('test', host='127.0.0.1', port=27017)


class PeopleDetailView(DetailView):
    template_name = PEOPLE_DETAIL

    def get_object(self, queryset=None):
        return People.objects.get(pk=self.kwargs['slug'])


class PeopleCreateView(FormView):
    form_class = PeopleForm
    template_name = PEOPLE_FORM
    success_url = reverse_lazy(LIST_PEOPLE)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        print(name, surname)
        person = People(name=name, surname=surname)
        person.save()
        return FormView.form_valid(self, form)


class PeopleUpdateView(FormView):
    form_class = PeopleForm
    template_name = PEOPLE_FORM
    success_url = reverse_lazy(LIST_PEOPLE)

    def get_initial(self):
        initial = super(PeopleUpdateView, self).get_initial()
        p = People.objects.get(pk=self.kwargs['slug'])
        initial['name'] = p.name
        initial['surname'] = p.surname
        initial['slug'] = self.kwargs['slug']
        return initial

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        if 'slug' not in kwargs:
            kwargs['slug'] = self.kwargs['slug']
        return kwargs

    def form_valid(self, form):
        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        print(name, surname)
        person = People.objects.get(pk=self.kwargs['slug'])
        person.name = name
        person.surname = surname
        person.save()
        return FormView.form_valid(self, form)


class PeopleListView(ListView):
    template_name = PEOPLE_LIST

    def get_queryset(self):
        return People.objects()
