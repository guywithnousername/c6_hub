from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('polls', views.poll, name = 'poll'),
    path('discuss', views.discuss, name = 'discuss'),
    path('discuss/<int:topic_id>/', views.topic, name = 'topic'),
    path('polls/<int:poll_id>/', views.pollform, name = 'pollform')
]