from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Tweet
from users.models import CustomUser
import re

# Create your views here.
def all_tweets(request):
    tweets = Tweet.objects.all().order_by('-posted_at')
    return render(request, 'all_tweets.html', {'tweets': tweets, 'current_user': request.user.id})

def post_tweet(request):
    if (request.method == 'POST'):
        content = request.POST['content']
        hashtags = request.POST['hashtags']

        tweet = Tweet(user=request.user, content=content, hashtags=hashtags, posted_at=timezone.now())
        tweet.save()
        return redirect('/')

    else:
        return render(request, 'post_tweet.html', {'current_user': request.user.id})

def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if (request.user.id != tweet.user.id):
        return  redirect('tweets')

    if (request.method == 'POST'):
        content = request.POST['content']
        hashtags = request.POST['hashtags']

        tweet.content = content
        tweet.hashtags = hashtags
        tweet.save()

        return redirect('specific_tweet', tweet_id)
    else:
        return render(request, 'edit_tweet.html', {'current_user': request.user.id, 'content': tweet.content, 'hashtags': tweet.hashtags})

def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if (request.user.id != tweet.user.id):
        return redirect('tweets')

    tweet.delete()
    return redirect('tweets')

def specific_tweet(request, tweet_id):  
    tweet =  get_object_or_404(Tweet, pk=tweet_id)

    own_tweet = tweet.user.id == request.user.id

    hashtags = re.findall(r'#\w+', tweet.hashtags)
    cleaned_hashtags = [tag[1:] for tag in hashtags]

    return render(request, 'specific_tweet.html', {'current_user': request.user.id, 'tweet': tweet, 'own_tweet': own_tweet, 'hashtags': cleaned_hashtags})

def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id);

    if request.user != user_to_follow:
        if user_to_follow.followers.filter(pk=request.user.pk).exists():
            user_to_follow.followers.remove(request.user)
        else:
            user_to_follow.followers.add(request.user)

    return redirect('profile', user_id)
