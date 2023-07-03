from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'scholar/index.html')

def login(request):
    return render(request, 'scholar/login.html')

def create_acc(request):
    return render(request, 'scholar/create_acc.html')

def home_page(request, id):
    return render(request, 'scholar/home.html', {
        "id": id
    })

def profile_page(request, id):
    return render(request, 'scholar/profile.html', {
        "id": id
    })

def post_page(request, id):
    return render(request, 'scholar/post.html', {
        "id": id
    })

def create_post(request):
    return render(request, 'scholar/create_post.html')

def search_page(request):
    return render(request, 'scholar/search_page.html')

def favorite_posts(request):
    return render(request, 'scholar/favorite_posts.html')