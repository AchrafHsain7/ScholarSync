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

def view_post_page(request, id):
    return render(request, 'scholar/view_post.html', {
        "id": id
    })
def private_messages_page(request, receiver_id):
    return render(request, 'scholar/private_messages.html', {
        "receiver_id": receiver_id
    })
def administrator_view_page(request):
    return render(request, 'scholar/administrator_view.html')
def about_page(request):
    return render(request, 'scholar/about.html')