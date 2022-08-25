from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<str:id>/', views.posts, name='posts'),
    path('signup/', views.signupform, name='signupform'),
    path('login/', views.loginfunc, name='login'),
    path('logout/', views.logoutfunc, name='logout'),
    path('post/', views.post, name='post'),
    path('friends/', views.friends, name='friends'),
    path('addFriend/', views.addFriend, name='addFriend'),
    path('unfriend/', views.unfriend, name='unfriend'),
    path('likepost/', views.likepost, name='likepost'),

]