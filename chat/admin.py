from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)    
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','user','desc')

@admin.register(Profile)    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user')
   
@admin.register(Friends)    
class FriendsAdmin(admin.ModelAdmin):
    list_display = ('id','user1','user2', 'timestamp')

@admin.register(LikedPost)    
class LikedPostAdmin(admin.ModelAdmin):
    list_display = ('id','user','post_id', 'liked')
