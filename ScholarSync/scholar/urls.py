from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:id>', views.home_page, name='home'),
    path('profile/<int:id>', views.profile_page, name='profile'),
]