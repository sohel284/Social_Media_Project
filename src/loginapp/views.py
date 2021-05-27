from django.contrib.auth import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from loginapp.froms import *
from loginapp.models import Follow, UserProfile
from postapp.forms import PostForm
from postapp.models import Post
# Create your views here.


def sign_up(request):
    form = CreateNewUserForm()
    registered = False
    if request.method == 'POST':
        form = CreateNewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user, )
            user_profile.save()
            return redirect('login_page')
    return render(request, 'login_app/signup.html', {
        'title': 'Sign Up Instragram', 'form': form,
    })

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password, )
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'login_app/login.html', {'title': 'Login', 'form':form, })

@login_required
def logout_user(request):
    logout(request)
    return redirect('login_page')    

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=current_user, )
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=current_user)
        print(form)
        if form.is_valid():
            form.save(commit=True, )
            form = UserProfileForm(instance=current_user, )
            print(form)
    return render(request, 'login_app/user_profile.html', {'title': 'Edit Profile. Social', 'form':form, })

@login_required
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, )
        print(form)
        if form.is_valid():
            post = form.save(commit=False, )
            post.author = request.user
            post.save()
            print(post)
            return redirect('home')
    return render(request, 'login_app/user.html', {'form': form, })

@login_required
def user(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_other)
    if user_other == request.user:
        print(user_other)
        print(request.user)
        return redirect('profile')
    return render(request, 'login_app/user_other.html', {'user_other': user_other, 'already_followed': already_followed})

def follow(request, username):
    following_user = User.objects.get(username=username, )
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user, )
        followed_user.save()
    return HttpResponseRedirect(reverse('user', kwargs={'username': username}))
    
def unfollow(request, username):
    following_user = User.objects.get(username=username, )
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('user', kwargs={'username': username}))
    


