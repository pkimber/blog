# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin
from blog.models import Post
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
  
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by(
        'published_date'
    )
    return render(request, 'blog/post_list.html', {'posts': posts})

class HomeView(BaseMixin, TemplateView):

    template_name = 'example/home.html'
