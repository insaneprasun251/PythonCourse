from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mat',
        'title': 'Blog Post 1',
        'content': 'First post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Matthew',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
