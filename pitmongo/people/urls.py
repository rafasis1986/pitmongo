# -*- coding: utf-8 -*-

from django.conf.urls import url
from pitmongo.people.views import PeopleListView, PeopleDetailView, PeopleUpdateView, PeopleDeleteView,\
    PeopleCreateView

app_name = 'people'
urlpeople = [
    url(regex=r'^~add/$', view=PeopleCreateView.as_view(), name='add'),
    # URL pattern for the PeopleListView
    url(regex=r'^$', view=PeopleListView.as_view(), name='list'),
    # URL pattern for the PeopleDetailView
    url(regex=r'^(?P<slug>[\w.@+-]+)/$', view=PeopleDetailView.as_view(), name='detail'),
    # URL pattern for the PeopleUpdateView
    url(regex=r'^~update/(?P<slug>[\w.@+-]+)/$', view=PeopleUpdateView.as_view(), name='update'),
    # URL pattern for the PeopleUpdateView
    url(regex=r'^~delete/(?P<slug>[\w.@+-]+)/$', view=PeopleDeleteView.as_view(), name='delete'),
]
