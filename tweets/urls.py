from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.all_tweets), name="tweets"),
    path('post-tweet', login_required(views.post_tweet), name="post_tweet"),
    path('edit-tweet/<int:tweet_id>', login_required(views.edit_tweet), name="edit_tweet"),
    path('delete-tweet/<int:tweet_id>', login_required(views.delete_tweet), name="delete_tweet"),
    path('tweets/<int:tweet_id>', login_required(views.specific_tweet), name="specific_tweet"),
    path('follow/<int:user_id>', login_required(views.follow_user), name="follow_user"),
]
