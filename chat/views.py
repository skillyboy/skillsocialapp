from django.http import JsonResponse
from . forms import SignupForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.shortcuts import render

# ===================LOGIN===================
def signupform(request):
    reg = SignupForm()
    if request.method == 'POST':
        reg = SignupForm(request.POST)
        if reg.is_valid():
            new = reg.save()
            login(request, new)
            new_profile = Profile(user= request.user)
            new_profile.save()
            messages.success(request, 'Signup successfull!')
            return redirect('home')
        else:
            messages.warning(request, reg.errors)
            return redirect('signupform')
    context = {
        'reg': reg
    }
    return render (request,'signup.html', context)

def logoutfunc(request):
    logout(request)
    return redirect('login')

def loginfunc(request):  
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            messages.success(request, "Welcome to my Assignment!")
            return redirect('home')
        else:
            return redirect('login')
    return render (request, 'login.html')

# ===================CONTENT===================
@login_required(login_url='login')
def home(request):
    friends= Friends.objects.all()
    context={
        'friends': friends,
    }  
    return render(request, 'index.html', context)

@login_required(login_url='login')
def posts(request,id):
    user2= Friends.objects.get(id=id)
    user2 = user2.user2
    posts = Post.objects.filter(user=user2)


    context = {
        # 'user_object': user_object,
        # 'user_profile': user_profile,
        'posts': posts,
        
    }
    return render(request, 'posts.html', context)

@login_required(login_url='login')
def friends(request):
    allusers= Profile.objects.all()
    friends = Friends.objects.all()
    context={
        'allusers': allusers,
        'friends': friends,
        

    }  
    return render(request, 'friends.html', context)

@login_required(login_url='login')
def post(request):
    if request.method == 'POST':
        desc = request.POST['desc']
        file = request.FILES.get('file')
        a = Post(desc=desc, file=file, user=request.user)
        a.save()
        messages.success(request, 'Posted successfully!')
        return redirect('home')
    else:
    	messages.error(request, 'Gist was not Posted successfully!')
        # return redirect('form')

@login_required(login_url='login')
def addFriend(request):
    # if request.method == "GET":
    
    name=request.POST['participant']
    friend = User.objects.get(username=name)
    curr_user = request.user
    # print(curr_user.username)

    group = (Friends.objects.filter(user1=curr_user, user2=friend) |
             Friends.objects.filter(user2=curr_user, user1=friend))

    if not group:
        obj = Friends(user1=curr_user, user2=friend)
        obj.save()
    messages.success(request, 'Friend added successfully')
    return redirect("friends")


@login_required(login_url='login')
def unfriend(request):
    itemid=request.POST['friend']
    Friends.objects.filter(pk=itemid).delete()
    messages.success(request, 'Friend deleted')
    return redirect ('friends')
  
@login_required(login_url='login')
def likepost(request):
    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        username = request.user.id
        username = User.objects.get(id=username)
        post=request.POST['post']
        post = Post.objects.get(pk=post)
        liked_filter = LikedPost.objects.filter(post_id=post, user=username)
        if liked_filter:    
            post.no_likes = post.no_likes - 1  
            LikedPost.objects.filter(post_id=post, user=username).delete()
            post.save() 
        else:    
            new_like =LikedPost.objects.create(post_id=post, user=username)
            new_like.save()
            post.no_likes = post.no_likes + 1  
            post.save()     
    return redirect(url)


