from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), # for users related stuff
    path('', include('tweets.urls')) # for tweets related stuff
]

admin.site.site_header = "Twitter Admin"
admin.site.site_title = "Twitter Admin Portal"
admin.site.index_title = "Welcome to Twitter"
