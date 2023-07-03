from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:id>', views.home_page, name='home'),
    path('profile/<int:id>', views.profile_page, name='profile'),
    path('login', views.login, name='login'),
    path('create_acc', views.create_acc, name='create_acc'),
    path('view_post/<int:id>', views.view_post_page, name='view_post'),
    path('private_messages/<int:receiver_id>', views.private_messages_page, name='private_messages'),
    path('administrator_view', views.administrator_view_page, name='administrator_view'),
    path('about', views.about_page, name='about'),
    
]