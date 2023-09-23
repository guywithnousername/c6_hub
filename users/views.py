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
    model = None
    redir = ""
    if type == "topic":
        model = apps.get_model("mainpage", "Topic").objects.get(id=id)
        redir = "mainpage:topic"
    if model.voted == None:
        model.voted = {request.user.username:0}
        
    voted = model.voted[request.user.username]
    if voted == 1:
        model.votes -= 1
        model.voted[request.user.username] = 0
    elif voted == -1:
        model.votes += 2
        model.voted[request.user.username] = 1
    else:
        model.votes += 1
        model.voted[request.user.username] = 1
    model.save()
    return redirect(redir, id)
    
@login_required
def votedown(request, type, id):
    model = None
    redir = ""
    if type == "topic":
        model = apps.get_model("mainpage", "Topic").objects.get(id=id)
        redir = "mainpage:topic"
    if model.voted == None:
        model.voted = {request.user.username:0}
    
    voted = model.voted[request.user.username]
    if voted == -1:
        model.votes += 1
        model.voted[request.user.username] = 0
    elif voted == 1:
        model.votes -= 2
        model.voted[request.user.username] = -1
    else:
        model.votes -= 1
        model.voted[request.user.username] = -1
    model.save()
    return redirect(redir, id)