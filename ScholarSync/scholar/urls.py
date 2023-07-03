from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:id>', views.home_page, name='home'),
    path('profile/<int:id>', views.profile_page, name='profile'),
    path('login', views.login, name='login'),
    path('create_acc', views.create_acc, name='create_acc'),
    path('post/<int:id>', views.post_page, name='post'),
    path('createpost', views.create_post, name='create_post'),
    path('searchpage', views.search_page, name='search_page'),
    path('favoriteposts', views.favorite_posts, name='favorite_posts'),

]