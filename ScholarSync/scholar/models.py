from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class User(AbstractUser):
    pass


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    secret_qst = models.CharField(max_length=100, null=True, blank=True)
    answer_qst = models.CharField(max_length=50, null=True, blank=True)
    friends = models.ManyToManyField(User, related_name='user_friends')
   
    def __str__(self) -> str:
        return f"{self.user.username}: {self.fname} {self.lname}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    date = models.DateTimeField(auto_now_add=True)
    image = models.URLField()
    description = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=500, blank=False)
    likes = models.ManyToManyField(User, related_name='user_liked_posts', null=True)

    def __str__(self):
        return f"{self.title} posted by {self.user} on {self.date}"
    

    




