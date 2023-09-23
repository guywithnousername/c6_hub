from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('notifications/', views.notifications, name='notifications'),
    path('upvote/<type>/<id>', views.voteup, name="upvote"),
    path('downvote/<type>/<id>', views.votedown, name="downvote"),
]