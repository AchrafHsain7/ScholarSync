from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class User(AbstractUser):
    pass


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    secret_qst = models.CharField(max_length=100, null=True)
    answer_qst = models.CharField(max_length=50, null=True)
   
    def __str__(self) -> str:
        return f"User: {self.user.username}, first name:{self.fname}, last name:{self.lname}"



    




