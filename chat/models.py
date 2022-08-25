from ast import Div
from concurrent.futures import process
from this import d
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import uuid


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=False)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    file=models.FileField(upload_to='post/', blank=True, null=True)
    liked = models.BooleanField(default=False)
    no_likes = models.IntegerField(default=False)
   
    def __str__(self):
        return self.desc
    
class LikedPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="LikedPost")
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="LikedPost")
    liked = models.BooleanField(default=False)
    
class Profile(models.Model):
    user = models.CharField(max_length=100)
   
    def __str__(self):
        return self.user
    
class Friends(models.Model):
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friends")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user1}"

    class Meta:
        ordering = ("timestamp",)
# ========================================================


        



