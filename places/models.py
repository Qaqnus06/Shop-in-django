from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    adress=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Owner(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    bio=models.TextField()
    # adress=models.CharField(max_length=200)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class PlaceOwner(models.Model):
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.place.name}  owner by {self.owner}"

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    comment_text=models.TextField()
    stars_given=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    def ___str__(self):
        return f"{self.user.username} komentariya  {self.place.name} va berdi {self.comment_text} {self.stars_given} yulduz"
    



