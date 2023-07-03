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