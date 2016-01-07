# -*- coding: utf-8 -*-

from django.conf.urls import url
from pitmongo.users.views import PeopleListView, PeopleDetailView, PeopleUpdateView, PeopleDeleteView,\
    PeopleCreateView


urlpatterns = [
    url(regex=r'^~add/$', view=PeopleCreateView.as_view(), name='people_add'),
    # URL pattern for the PeopleListView
    url(regex=r'^$', view=PeopleListView.as_view(), name='people_list'),
    # URL pattern for the PeopleDetailView
    url(regex=r'^(?P<slug>[\w.@+-]+)/$', view=PeopleDetailView.as_view(), name='people_detail'),
    # URL pattern for the PeopleUpdateView
    url(regex=r'^~update/(?P<slug>[\w.@+-]+)/$', view=PeopleUpdateView.as_view(), name='people_update'),
    # URL pattern for the PeopleUpdateView
    url(regex=r'^~delete/$', view=PeopleDeleteView.as_view(), name='people_delete'),
]
