from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    city = models.CharField(max_length=50, blank=False)
    secret_qst = models.CharField(max_length=100, null=True)
    answer_qst = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f"User: {self.username}, first name:{self.fname}, last name:{self.lname}"


    

        
class Post(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")



