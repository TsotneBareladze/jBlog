from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
#   return render(request, 'home.html', {})


class HomeView(ListView):#HomeView is just name not smthing system Name
    model = Post
    template_name = "BlogApp/home.html"
    ordering = ['-id']#Post are ordered by id
    ordering = ['post_date']  # Post are ordered by id


class ArticleDetailView(DetailView):#ArticleDetailView is just name not smthing system Name
    model = Post
    template_name = 'BlogApp/article_details.html'

class AddPostView(CreateView):#AddPostView is just name not smthing system Name
    model = Post
    form_class = PostForm
    template_name = 'BlogApp/add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'BlogApp/update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'BlogApp/delete_post.html'
    success_url = reverse_lazy('home')