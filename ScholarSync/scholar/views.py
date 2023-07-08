from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import *









#login user
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'scholar/login.html', {
            "erorr_message": "Invalid username and/or password"
        })


    else:
        return render(request, 'scholar/login.html')
    






# Create your views here.
def index(request):
    if request.user.is_autheticated:
        return render(request, 'scholar/index.html')
    else:
        return HttpResponseRedirect(reverse('login'))
    




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
    return render(request, 'scholar/view_post.html', {
        "id": id
    })

def create_post(request):
    return render(request, 'scholar/create_post.html')

def search_page(request):
    return render(request, 'scholar/search_page.html')

def favorite_posts(request):
    return render(request, 'scholar/favorite_posts.html')

def private_messages_page(request, receiver_id):
    return render(request, 'scholar/private_messages.html', {
        "receiver_id": receiver_id
    })

def administrator_view_page(request):
    return render(request, 'scholar/administrator_view.html')

def about_page(request):
    return render(request, 'scholar/about.html')

