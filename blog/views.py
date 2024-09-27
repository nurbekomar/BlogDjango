from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
# Create your views here.

menu = ['Блог', 'Проекты', 'О нас']


def index(request):
    posts = Blog.objects.all()
    return render(request, 'blog/index.html', {'title': 'BlogNurbek', 'menu': menu, 'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About NurbekTech', 'menu': menu})
