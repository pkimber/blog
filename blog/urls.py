# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)

from .views import BlogView


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=BlogView.as_view(),
        name='blog.list'
        ),
)
