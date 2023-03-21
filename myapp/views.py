from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView


# def greet(request):
#     return HttpResponse("Hi there! welcome to mazi's django class")

def greet(request):
    posts = Post.objects.all()
    return render(request, 'myapp/welcome.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myapp/post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'myapp/post_detail.html'
    context_object_name = 'post'


def passion(request):
    return HttpResponse("i love programming")


class PostListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = 'myapp/post_new.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'myapp/post_delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'myapp/post_update.html'
    fields = ['title', 'body']

# Create your views here.
