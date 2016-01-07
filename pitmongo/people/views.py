# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView

from pitmongo.people.models import People


LIST_PEOPLE = 'people:list'
OBJ_NAME = 'object_name'
OBJ_TEMP = 'object_template'
PEOPLE_DELETE = ''
PEOPLE_DETAIL = 'users/people_detail.html'
PEOPLE_FORM = 'users/people_form.html'
PEOPLE_LIST = 'users/people_list.html'
PEOPLE_NAME = 'people'
PEOPLE_TEMP = PEOPLE_NAME


class PeopleMixin(object):
    model = People


class PeopleFormMixin(PeopleMixin):
    fields = ['name', 'surname']


class PeopleDetailView(PeopleMixin, DetailView):
    pass


class PeopleCreateView(PeopleFormMixin, CreateView):
    pass


class PeopleUpdateView(PeopleFormMixin, UpdateView):
    pass


class PeopleListView(PeopleMixin, ListView):
    pass


class PeopleDeleteView(PeopleMixin, DeleteView):
    success_url = reverse_lazy(LIST_PEOPLE)
