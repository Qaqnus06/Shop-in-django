from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo=models.ImageField(upload_to="user_photos/",default="")
    photo_numb=models.CharField(max_length=13, unique=True,null=True,blank=True)
    friends=models.ManyToManyField('user.User',blank=True)

class FriendRequest(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='from_user')
    to_user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='to_user')
    is_accepted=models.BooleanField(default=False)


