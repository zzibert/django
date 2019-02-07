from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Corey',
        'title': 'Blog post 1',
        'content': 'First post content',
        'data_posted': 'August, 27, 2018'
    },
    {
        'author': 'Winston',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'data_posted': 'August, 27, 2018'
    },
    {
        'author': 'Balthazar',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'data_posted': 'August, 27, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'about something page'
    }
    return render(request, 'blog/about.html', context)

