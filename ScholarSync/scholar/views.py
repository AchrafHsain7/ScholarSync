from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required


from .models import *



#forms templates go here
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    fname = forms.CharField(max_length=50, required=True)
    lname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=70, required=True)
    city = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)

class PostForm(forms.Form): 
    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=200, required=False)
    content = forms.CharField(max_length=500, required=True)
    imageURL = forms.URLField(required=False) 





#login user
#to add: The secret question verification
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'scholar/login.html', {
            "erorr_message": "Invalid username and/or password"
        })
    else:
        return render(request, 'scholar/login.html')
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'scholar/index.html', {
            "posts": posts,
        })   
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

            try:
                user = User.objects.create_user(username, email,  password) 
                profile = Profile.objects.create(
                    user=user,
                    fname=fname,
                    lname=lname,
                    city=city,
                    #secret_qst='Favorite color?',
                    #answer_qst='Blue',
                )
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('index'))  
            except:
                return render(request, 'scholar/create_acc.html', {
                    "form": RegistrationForm(request.POST),
                    "err_message": "This username already exist"
        })

        else:
            return render(request, 'scholar/create_acc.html', {
            "form": RegistrationForm(request.POST),
            "err_message": "Invalid Fields"
        })

    else:
        return render(request, 'scholar/create_acc.html', {
            "form": RegistrationForm()
        })





#to be done later
def home_page(request, id):
    return render(request, 'scholar/home.html', {
        "id": id
    })


@login_required(login_url='login')
def profile_page(request):
    return render(request, 'scholar/profile.html', {
        "username": request.user.username,
        "fname": request.user.user_profile.fname,
        "lname": request.user.user_profile.lname,
        "city": request.user.user_profile.city,
        "secret_qst":  request.user.user_profile.secret_qst
    })
#to add: possibility to edit the profile


@login_required(login_url='login')
def post_page(request, id):
    post = Post.objects.filter(id=id).first()
    likes = post.likes.all().count()
    return render(request, 'scholar/view_post.html', { 
        "post": post, 
        "num_likes":  likes 
    })




@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        form_response = PostForm(request.POST)
        if form_response.is_valid():
            title = form_response.cleaned_data["title"]
            description = form_response.cleaned_data["description"]
            content = form_response.cleaned_data["content"]
            imageURL = form_response.cleaned_data["imageURL"]

            #try:
            post = Post.objects.create(
                user=request.user,
                image =imageURL,
                title=title,
                description=description,
                content=content,
            )
            post.save()
            return HttpResponseRedirect(reverse('index'))
            

        else:
            return render(request, 'scholar/create_post.html', {
                "form": PostForm(request.POST),
                "err_message": "Invalid Fields found"
            })

    else:
        return render(request, 'scholar/create_post.html', {
            "form": PostForm()
        })
    
@login_required(login_url='login')
def like_post(request, id):
    if request.method == 'POST':
        post = Post.objects.filter(id=id).first()
        if post is not None:
            post.likes.add(request.user)
            return HttpResponseRedirect(reverse('post', args=(id, ))) 
        else:
            return HttpResponseRedirect(reverse('index'))
    else: 
        return HttpResponseRedirect(reverse('index'))






@login_required(login_url='login')
def view_friends(request):
    return render(request, 'view_friends.html', {
        
    })


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

