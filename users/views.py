from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.apps import apps

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mainpage:index')
    context = {"form":form}
    return render(request, "registration/register.html", context)

@login_required
def notifications(request):
    if not hasattr(request.user, "notification"):
        Notification.objects.create(user=request.user, unread = [], read=True)
    request.user.notification.read = True
    request.user.notification.save()
    context = {"notifs":request.user.notification.unread}
    return render(request, "users/notifications.html", context)

@login_required
def voteup(request, type, id):
    if type == "topic":
        topic = apps.get_model("mainpage", "Topic").objects.get(id=id)
        topic.votes += 1
        topic.save()
        return redirect("mainpage:topic", id)
    
@login_required
def votedown(request, type, id):
    if type == "topic":
        topic = apps.get_model("mainpage", "Topic").objects.get(id=id)
        topic.votes -= 1
        topic.save()
        return redirect("mainpage:topic", id)