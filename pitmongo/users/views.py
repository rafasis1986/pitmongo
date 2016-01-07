# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView

from pitmongo.users.forms import PeopleForm
from pitmongo.users.models import People


LIST_PEOPLE = 'people_list'
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

    def get_context_data(self, **kwargs):
        kwargs.update({OBJ_NAME: PEOPLE_NAME})
        kwargs.update({OBJ_TEMP: PEOPLE_TEMP})
        return kwargs


class PeopleFormMixin(PeopleMixin):
    form_class = PeopleForm
    template_name = PEOPLE_FORM


class PeopleDetailView(PeopleMixin, DetailView):
    template_name = PEOPLE_DETAIL


class PeopleCreateView(PeopleFormMixin, CreateView):

    def form_valid(self, form):
        respuesta = None
        self.object = form.save(commit=True)
        if self.object:
            #=======================================================================================
            # messages.error(self.request, MSG_VEHICULO_FUERA_RANGO % ( self.object.flotaVehiculo, annoMin, annoMax))
            #=======================================================================================
            respuesta = CreateView.form_valid(self, form)
        else:
            #=======================================================================================
            # messages.success(self.request, MSG_VEHICULO_SUCCESS)
            #=======================================================================================
            respuesta = CreateView.form_invalid(self, form)
        return respuesta
    
    def post(self, request, *args, **kwargs):
        return CreateView.post(self, request, *args, **kwargs)


class PeopleUpdateView(PeopleFormMixin, UpdateView):

    def get_object(self, queryset=None):
        return UpdateView.get_object(self, queryset=queryset)

class PeopleListView(PeopleMixin, ListView):
    template_name = PEOPLE_LIST
    slug_field = "slug"
    slug_url_kwarg = "slug"
    
    def get(self, request, *args, **kwargs):
        response = ListView.get(self, request, *args, **kwargs)
        return response

    
    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(PeopleListView, self).get_context_data(**context)


class PeopleDeleteView(PeopleMixin, DeleteView):
    template_name = PEOPLE_DELETE

    def get_success_url(self):
        return reverse(LIST_PEOPLE)
