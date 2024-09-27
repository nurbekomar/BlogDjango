from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
# Create your views here.

menu = [{'title': 'Blog', 'url_name': 'blog'},
        {'title': 'Project', 'url_name': 'project'},
        {'title': 'About', 'url_name': 'about'}
        ]


def index(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'blog/index.html', context=context)


def blog(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'blog/blog.html', context=context)


def show_post(request, post_id):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'blog/show_post.html', context=context)


def project(request):
    context = {
        'menu': menu,
    }
    return render(request, 'blog/project.html', context=context)


def about(request):
    context = {
        'menu': menu,
    }
    return render(request, 'blog/about.html', context=context)
