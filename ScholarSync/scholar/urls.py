from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:id>', views.home_page, name='home'),
    path('profile', views.profile_page, name='profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('create_acc', views.create_acc, name='create_acc'),
    path('post/<int:id>', views.post_page, name='post'),
    path('createpost', views.create_post, name='create_post'),
    path('like_post/<int:id>', views.like_post, name="like_post"),
    path('friends', views.view_friends, name='friends'),
    path('friendProfile/<int:id>', views.friend_profile, name='friend_profile'),
    path('searchFriends', views.search_friends, name='search_friends'),
    path('add_friend/<int:id>', views.add_friend, name='add_friend'),
    path('remove_friend/<int:id>', views.remove_friend, name='remove_friend'),
    path('addComment/<int:id>', views.add_comment, name='add_comment'),
    path('deleteComment/<int:comment_id>/<int:post_id>', views.delete_comment, name='delete_comment'),
    path('searchPost', views.search_post, name='search_post'),
    path('favoriteposts', views.favorite_posts, name='favorite_posts'),
    path('addFavoritePost/<int:id>', views.add_favorite, name='add_favorite_posts'),
    path('myPosts', views.my_posts, name='my_posts'),
    path('deletePost/<int:id>', views.delete_post, name='delete_post'),
    path('editProfile', views.edit_profile, name='edit_profile'),   
    path('private_messages/<int:receiver_id>', views.private_messages_page, name='private_messages'),
    path('conversations', views.current_conversations, name='conversations'),

    path('administrator_view', views.administrator_view_page, name='administrator_view'),
    path('about', views.about_page, name='about'),
    
]