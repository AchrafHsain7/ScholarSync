from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:id>', views.home_page, name='home'),
    path('profile/<int:id>', views.profile_page, name='profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('create_acc', views.create_acc, name='create_acc'),
    path('post/<int:id>', views.post_page, name='post'),
    path('createpost', views.create_post, name='create_post'),
    path('searchpage', views.search_page, name='search_page'),
    path('favoriteposts', views.favorite_posts, name='favorite_posts'),
    path('private_messages/<int:receiver_id>', views.private_messages_page, name='private_messages'),
    path('administrator_view', views.administrator_view_page, name='administrator_view'),
    path('about', views.about_page, name='about'),
    
]