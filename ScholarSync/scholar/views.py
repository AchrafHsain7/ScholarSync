from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.contrib.auth.hashers import check_password


from .models import *



#forms templates go here
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    fname = forms.CharField(max_length=50, required=True)
    lname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=70, required=True)
    city = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)
    image = forms.URLField(required=False)

class PostForm(forms.Form): 
    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'rows':5, 'cols':50})) 
    content = forms.CharField(max_length=2000, required=True, widget=forms.Textarea(attrs={'rows':20, 'cols':100})) 
    imageURL = forms.URLField(required=False) 

class CommentForm(forms.Form):
    content = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={'rows':10, 'cols': 50}))

class SearchPostForm(forms.Form):
    search_query = forms.CharField(max_length=50, required=True) 








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
        "user_page": request.user,  
    })
#to add: possibility to edit the profile


@login_required(login_url='login')
def post_page(request, id):
    post = Post.objects.filter(id=id).first()
    likes = post.likes.all().count()
    comments = Comment.objects.filter(post=post).all() 
    return render(request, 'scholar/view_post.html', { 
        "post": post, 
        "num_likes":  likes,
        'comment_form': CommentForm(),
        "comments": comments,
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
    friends = request.user.user_profile.friends.all()
    return render(request, 'scholar/view_friends.html', {
        "friends": friends
    }) 

@login_required(login_url='login')
def friend_profile(request, id):
    friend = User.objects.filter(id=id).first()
    if friend is not None:
        return render(request, 'scholar/profile.html', {
            "user_page": friend,
        })
    else:  
        return HttpResponseRedirect(reverse('index'))
    


@login_required(login_url='login')
def search_friends(request):
    if request.method == 'POST':
        username = request.POST['username']
        if username != '':
            users_found = User.objects.filter(username__contains=username)
            friends = request.user.user_profile.friends.all()
            return render(request, 'scholar/view_friends.html', {
                "friends": friends,
                "search_data": users_found
            })
        else:
            return HttpResponseRedirect(reverse('friends')) 

    else:
        return HttpResponseRedirect(reverse('index'))
    
@login_required(login_url='login')
def add_friend(request, id):
    if request.method == 'POST':
        friend = User.objects.filter(id=id).first()
        if friend is not None:
            request.user.user_profile.friends.add(friend) 
            return HttpResponseRedirect(reverse('friends'))  
        else:
            return HttpResponseRedirect(reverse(index))
    else:
        return HttpResponseRedirect(reverse(index))


@login_required(login_url='login')
def remove_friend(request, id):
    if request.method == 'POST':
        friend = User.objects.filter(id=id).first()
        if friend is not None:
            request.user.user_profile.friends.remove(friend)
            return HttpResponseRedirect(reverse('friends'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url='login')
def add_comment(request, id):
    if request.method == 'POST':  
        post = Post.objects.filter(id=id).first()
        if post is not None:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = Comment.objects.create(
                    post=post ,
                    user=request.user,  
                    content=comment_form.cleaned_data['content']
                    )    
                comment.save()
                return HttpResponseRedirect(reverse('post', args=(id, ))) 
            else:
                return HttpResponseRedirect(reverse('post', args=(id, ))) 
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))  
#WTF is this 

@login_required(login_url='login')
def delete_comment(request, comment_id, post_id):
    if request.method == 'POST':
        comment = Comment.objects.filter(id=comment_id).first() 
        if comment is not None:
            comment.delete()
            return HttpResponseRedirect(reverse('post', args=(post_id, )))   
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))





#@login_required(login_url='login')
def search_post(request):

    if request.method == 'POST':
        search_form = SearchPostForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['search_query']
            search_query = Q(title__contains=query) | Q(description__contains=query) | Q(content__contains=query) | Q(user__username__contains=query)
            posts = Post.objects.filter(search_query).all()
            return render(request, 'scholar/search_post.html', {
                'search_form': SearchPostForm(request.POST),     
                'search_result': posts
            })
        else:
            return render(request, 'scholar/search_post.html', {
            'search_form': SearchPostForm(request.POST),
        })


    else:
        return render(request, 'scholar/search_post.html', {
            'search_form': SearchPostForm(),
        })





@login_required(login_url='login')
def favorite_posts(request):
    favorites = request.user.favorite_posts.all()
    return render(request, 'scholar/favorite_posts.html', {
        "posts": favorites
    })
  
@login_required(login_url='login')
def add_favorite(request, id):
    if request.method == 'POST':
        post = Post.objects.filter(id=id).first()
        if post is not None:
            request.user.favorite_posts.add(post)
            return HttpResponseRedirect(reverse('favorite_posts')) 
        else:
            return HttpResponseRedirect(reverse('index')) 
       
    else:
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url='login')
def my_posts(request):
    posts = request.user.user_posts.all()
    return render(request, 'scholar/my_posts.html', {
        'posts': posts
    })

@login_required(login_url='login')
def delete_post(request, id):
    if request.method == 'POST':
        post = Post.objects.filter(id=id).first()
        if post is not None:
            post.delete()
            return HttpResponseRedirect(reverse('my_posts'))
        else:
            return HttpResponseRedirect(reverse('my_posts'))
    else:
        return HttpResponseRedirect(reverse('index'))


@login_required(login_url='login')
def edit_profile(request):

    if request.method == 'POST':
        edit_form = RegistrationForm(request.POST)
        if edit_form.is_valid():
            try:
                user = request.user
                if check_password(edit_form.cleaned_data['password'], user.password):
                    user.username = edit_form.cleaned_data['username']
                    user.user_profile.fname = edit_form.cleaned_data['fname']
                    user.user_profile.lname = edit_form.cleaned_data['lname']
                    user.user_profile.email = edit_form.cleaned_data['email']
                    user.user_profile.city = edit_form.cleaned_data['city']
                    user.save()
                    return HttpResponseRedirect(reverse('profile'))  
                else:
                    return render(request, 'scholar/edit_profile.html', {
                        "form": RegistrationForm(request.POST),  
                        "err_message": "Wrong Password" 
                    })
            except:
                return render(request, 'scholar/edit_profile.html', {
            "form": RegistrationForm(request.POST),  
            "err_message": "This username is already taken" 
        })

        else:
            return render(request, 'scholar/edit_profile.html', {
            "form": RegistrationForm(request.POST),   
        })

    else:
        return render(request, 'scholar/edit_profile.html', {
            "form": RegistrationForm(),   
        })






def private_messages_page(request, receiver_id):
    return render(request, 'scholar/private_messages.html', {
        "receiver_id": receiver_id
    })

def administrator_view_page(request):
    return render(request, 'scholar/administrator_view.html')

def about_page(request):
    return render(request, 'scholar/about.html')

