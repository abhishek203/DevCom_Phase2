
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
    def save(self,commit=True):
        blog_post=self.instance
        blog_post.title=self.cleaned_data['title']
        blog_post.content=self.cleaned_data['content']
        if commit:
            blog_post.save()
        return blog_post
