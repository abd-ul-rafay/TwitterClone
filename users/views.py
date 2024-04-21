from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from .models import CustomUser
from tweets.models import Tweet

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

def profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    tweets = Tweet.objects.filter(user=user).order_by('-posted_at')

    is_following = user.followers.filter(pk=request.user.pk).exists()

    return render(request, 'profile.html', { 'user': user, 'current_user': request.user.id, 'tweets': tweets, 'is_following': is_following })
