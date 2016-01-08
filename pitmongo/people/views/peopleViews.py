# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, DeleteView

from pitmongo.people.forms import PeopleForm
from pitmongo.people.models import People, Profetion
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


LIST_PEOPLE = 'people:list'
OBJ_NAME = 'object_name'
OBJ_TEMP = 'object_template'
PEOPLE_DELETE = 'people/people_confirm_delete.html'
PEOPLE_DETAIL = 'people/people_detail.html'
PEOPLE_FORM = 'people/people_form.html'
PEOPLE_LIST = 'people/people_list.html'
PEOPLE_NAME = 'people'
PEOPLE_TEMP = PEOPLE_NAME


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
        profetionPk = form.cleaned_data['profetion']
        profetion = Profetion.objects.get(pk=profetionPk)
        person = People(name=name, surname=surname, profetion=profetion)
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
        try:
            initial['profetion'] = p.profetion.pk
        except:
            pass
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
        profetionPk = form.cleaned_data['profetion']
        profetion = Profetion.objects.get(pk=profetionPk)
        People.objects.get(pk=self.kwargs['slug']).update(name=name, surname=surname, profetion=profetion)
        return FormView.form_valid(self, form)


class PeopleListView(ListView):
    template_name = PEOPLE_LIST
    paginate_by = 15

    def get_queryset(self):
        criteria = self.request.GET.get('criteria', None)
        if criteria:
            return People.objects().search_text(criteria.strip()).order_by('name','surname')
        return People.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        people = self.get_queryset()
        paginator = Paginator(people, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            people = paginator.page(page)
        except PageNotAnInteger:
            people = paginator.page(1)
        except EmptyPage:
            people = paginator.page(paginator.num_pages)
        context['object_list'] = people
        return context


class PeopleDeleteView(DeleteView):
    template_name = PEOPLE_DELETE
    success_url = reverse_lazy(LIST_PEOPLE)

    def get_object(self, queryset=None):
        return People.objects.get(pk=self.kwargs['slug'])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
