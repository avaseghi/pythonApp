# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from records.models import Post

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

class PostListView(ListView):

    model = Post

class PostDetailView(DetailView):

    model = Post

class CreatePostView(CreateView):

    model = Post
    fields = ['title', 'slug', 'content', 'image']

class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('list_posts')

# Create your views here.
