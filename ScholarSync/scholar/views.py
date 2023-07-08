from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms


from .models import *



#forms templates go here
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    fname = forms.CharField(max_length=50, required=True)
    lname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=70, required=True)
    city = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)





#login user
#to add: The secret question verification
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password)

        if user.first() != None:
            request.session["is_authenticated"] = True
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'scholar/login.html', {
            "erorr_message": "Invalid username and/or password"
        })

    else:
        return render(request, 'scholar/login.html')
    




# Create your views here.
def index(request):
    if "is_autheticated" not in request.session.keys():
        request.session["is_autheticated"] = False
        return HttpResponseRedirect(reverse('login'))
    
    if request.session["is_authenticated"] == True:
        return render(request, 'scholar/index.html')
    else:
        return HttpResponseRedirect(reverse('login'))
    




def create_acc(request):
    if request.method == 'POST':
        form_response = RegistrationForm(request.POST)
        if form_response.is_valid():
            username = form_response.cleaned_data["username"]
            fname = form_response.cleaned_data["fname"]
            lname = form_response.cleaned_data["lname"]
            email = form_response.cleaned_data["email"]
            city = form_response.cleaned_data["city"]
            password = form_response.cleaned_data["password"]
            user = User(username=username, password=password, fname=fname, lname=lname, email=email, city=city)
            user.save()
            request.session["is_authenticated"] = True
            return HttpResponseRedirect(reverse('index'))  
        else:
            return render(request, 'scholar/create_acc.html', {
            "form": RegistrationForm(request.POST),
            "err_message": "Invalid Fields"
        })

    else:
        return render(request, 'scholar/create_acc.html', {
            "form": RegistrationForm()
        })






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

