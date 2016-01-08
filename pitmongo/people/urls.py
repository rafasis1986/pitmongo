# -*- coding: utf-8 -*-

from django.conf.urls import url

from pitmongo.people.views.peopleViews import PeopleListView, PeopleDetailView, PeopleUpdateView, PeopleCreateView, \
    PeopleDeleteView
from pitmongo.people.views.profetionViews import ProfetionCreateView, ProfetionListView, \
    ProfetionDetailView, ProfetionUpdateView, ProfetionDeleteView


app_name = 'people'
urlpeople = [
    url(regex=r'^~add/$', view=PeopleCreateView.as_view(), name='add'),
    url(regex=r'^$', view=PeopleListView.as_view(), name='list'),
    url(regex=r'^(?P<slug>[\w.@+-]+)/$', view=PeopleDetailView.as_view(), name='detail'),
    url(regex=r'^~update/(?P<slug>[\w.@+-]+)/$', view=PeopleUpdateView.as_view(), name='update'),
    url(regex=r'^~delete/(?P<slug>[\w.@+-]+)/$', view=PeopleDeleteView.as_view(), name='delete'),
    url(regex=r'^profetion/add/$', view=ProfetionCreateView.as_view(), name='pro-add'),
    url(regex=r'^profetions$', view=ProfetionListView.as_view(), name='pro-list'),
    url(regex=r'^profetion/(?P<slug>[\w.@+-]+)/$', view=ProfetionDetailView.as_view(), name='pro-detail'),
    url(regex=r'^profetion/update/(?P<slug>[\w.@+-]+)/$', view=ProfetionUpdateView.as_view(), name='pro-update'),
    url(regex=r'^profetion/delete/(?P<slug>[\w.@+-]+)/$', view=ProfetionDeleteView.as_view(), name='pro-delete'),
]
