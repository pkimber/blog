# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from .views import BlogView
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.post_list, name='blog.list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
)
