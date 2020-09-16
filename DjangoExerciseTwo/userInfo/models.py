from django.db import models
from django.contrib.auth.models import User as User_default
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,blank=True)
    last_name = models.CharField(max_length=264, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name

class UserProfile(models.Model):
    user = models.OneToOneField(User_default,on_delete=models.CASCADE)

    #additional

    porfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
