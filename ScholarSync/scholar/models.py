from django.db import models

# Create your models here.

class User(models.Model):
    user_fname = models.CharField(max_length=50, blank=False)
    user_lname = models.CharField(max_length=50, blank=False)
    user_email = models.EmailField(max_length=70, blank=False)
    user_city = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    secret_qst = models.CharField(max_length=100, null=True)
    answer_qst = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f"User: {self.username}, first name:{self.user_fname}, last name:{self.user_lname}"


    

        
class Post(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")



