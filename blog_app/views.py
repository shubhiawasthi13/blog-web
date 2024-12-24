from django.shortcuts import render, redirect
from . import models
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    context ={
        'posts':Posts.objects.all()
    }
    return render(request, 'blog_app/home.html',context)

def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username = name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home')
        else:
            return redirect('/loginn')
    return render(request, 'blog_app/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser =User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/login')
    return render(request, 'blog_app/signup.html')

def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        newPost = models.Posts(title= title, content=content, author = request.user)
        newPost.save()
        return redirect('/home')
    return render(request, 'blog_app/newpost.html')

def signout(request):
    logout(request)
    return redirect('/loginn')


def mypost(request):
    context ={
        'posts':Posts.objects.filter(author = request.user)
    }
    return render(request, 'blog_app/mypost.html',context)