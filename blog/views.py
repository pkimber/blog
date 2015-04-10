# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView

from base.view_utils import BaseMixin

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from .forms import ConfirmForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
  
@login_required    
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by(
        'published_date'
    )
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required       
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required    
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ConfirmForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('blog.views.post_list')
    else:
        form = ConfirmForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class BlogView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'blog/home.html'
    
    



