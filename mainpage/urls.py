from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name = 'index'),
    # find models
    path('polls', views.poll, name = 'poll'),
    path('discuss', views.discuss, name = 'discuss'),
    # view models
    path('discuss/<int:topic_id>/', views.topic, name = 'topic'),
    path('polls/<int:poll_id>/', views.pollform, name = 'pollform'),
    path('viewpoll/<int:poll_id>/', views.viewpoll, name= 'viewpoll'),
    # create models
    path('createtopic/', views.newtopic, name='newtopic'),
    path('createcomment/<int:topic_id>', views.newcomment, name='newcomment')
]