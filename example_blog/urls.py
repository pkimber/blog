# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from .views import HomeView
from . import views


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', views.post_list, name='project.home'),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(r'^home/user/$',
        view=RedirectView.as_view(url=reverse_lazy('blog.list')),
        name='project.dash'
        ),
    url(regex=r'^blog/',
        view=include('blog.urls')
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user

urlpatterns += staticfiles_urlpatterns()
