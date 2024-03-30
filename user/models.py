from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo=models.ImageField(upload_to="user_photos/",default="")
    photo_numb=models.CharField(max_length=13, unique=True,null=True,blank=True)




