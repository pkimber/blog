# -*- encoding: utf-8 -*-
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        
class ConfirmForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ()
