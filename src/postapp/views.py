from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from postapp.models import Like, Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    liked_post = Like.objects.filter(user=request.user)
    already_liked_list = liked_post.values_list('post', flat=True, )
    if request.method == 'GET':
        search = request.GET.get('search', '')
        results = User.objects.filter(username__icontains=search, ) 
    return render(request, 'home.html', {'search': search, 'results':results, 'posts':posts, 'already_liked_list':already_liked_list})

def liked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user, )
    if not already_liked:
        post_liked = Like(post=post, user=request.user)
        post_liked.save()
    return redirect('home')

def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user, )
    already_liked.delete()
    return redirect('home')

