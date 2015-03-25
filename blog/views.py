# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)


class BlogView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'blog/home.html'
