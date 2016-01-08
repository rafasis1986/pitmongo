# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, DeleteView

from pitmongo.people.forms import ProfetionForm
from pitmongo.people.models import Profetion
from mongoengine.errors import NotUniqueError
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect


LIST_PROFETION = 'people:pro-list'
OBJ_NAME = 'object_name'
OBJ_TEMP = 'object_template'
PROFETION_DELETE = 'people/profetion_confirm_delete.html'
PROFETION_DETAIL = 'people/profetion_detail.html'
PROFETION_FORM = 'people/profetion_form.html'
PROFETION_LIST = 'people/profetion_list.html'
PROFETION_NAME = 'profetion'
PROFETION_TEMP = PROFETION_NAME


class ProfetionDetailView(DetailView):
    template_name = PROFETION_DETAIL

    def get_object(self, queryset=None):
        return Profetion.objects.get(pk=self.kwargs['slug'])


class ProfetionCreateView(FormView):
    form_class = ProfetionForm
    template_name = PROFETION_FORM
    success_url = reverse_lazy(LIST_PROFETION)

    def form_valid(self, form):
        name = form.cleaned_data['name']
        profetion = Profetion(name=name)
        try:
            profetion.save()
        except NotUniqueError:
            messages.error(self.request, "previously added profession")
            return FormView.form_invalid(self, form)
        return FormView.form_valid(self, form)


class ProfetionUpdateView(FormView):
    form_class = ProfetionForm
    template_name = PROFETION_FORM
    success_url = reverse_lazy(LIST_PROFETION)

    def get_initial(self):
        initial = super(ProfetionUpdateView, self).get_initial()
        p = Profetion.objects.get(pk=self.kwargs['slug'])
        initial['name'] = p.name
        initial['slug'] = self.kwargs['slug']
        return initial

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        if 'slug' not in kwargs:
            kwargs['slug'] = self.kwargs['slug']
        return kwargs

    def form_valid(self, form):
        name = form.cleaned_data['name'].strip().upper()
        try:
            Profetion.objects.get(pk=self.kwargs['slug']).update(name=name)
        except NotUniqueError:
            messages.error(self.request, "previously added profession")
            return FormView.form_invalid(self, form)
        return FormView.form_valid(self, form)


class ProfetionListView(ListView):
    template_name = PROFETION_LIST
    paginate_by = 15

    def get_queryset(self):
        criteria = self.request.GET.get('criteria', None)
        if criteria:
            return Profetion.objects(name=criteria.strip().upper()).order_by('name')
        return Profetion.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ProfetionListView, self).get_context_data(**kwargs)
        profetion = self.get_queryset()
        paginator = Paginator(profetion, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            profetion = paginator.page(page)
        except PageNotAnInteger:
            profetion = paginator.page(1)
        except EmptyPage:
            profetion = paginator.page(paginator.num_pages)
        context['object_list'] = profetion
        return context


class ProfetionDeleteView(DeleteView):
    template_name = PROFETION_DELETE
    success_url = reverse_lazy(LIST_PROFETION)

    def get_object(self, queryset=None):
        return Profetion.objects.get(pk=self.kwargs['slug'])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
