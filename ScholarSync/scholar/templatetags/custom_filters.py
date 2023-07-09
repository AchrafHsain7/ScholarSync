from django import template

register = template.Library()

@register.filter
def is_friend_post(user, post_user):
    return (user.user_profile.friends.filter(id=post_user.id).exists() or user == post_user)

