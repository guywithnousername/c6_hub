from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'mainpage/index.html')

def poll(request):
    polls = Poll.objects.order_by('-date_added')
    context = {'polls':polls}
    return render(request, 'mainpage/poll.html', context)

def discuss(request):
    topics = Topic.objects.order_by('-date_added')
    context = {'topics':topics}
    return render(request, 'mainpage/discuss.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = topic.comment_set.order_by('-date_added')
    context = {'topic':topic, 'comments':comments}
    return render(request, 'mainpage/topic.html', context)

@login_required
def pollform(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.user.username in poll.values.keys():
        return redirect('mainpage:viewpoll', poll_id)
    choices = []
    i = 0
    for c in poll.choices:
        choices.append([i, c])
        i += 1
    if request.method != 'POST':
        form = PollForm()
        form.fields["choice"] = forms.ChoiceField(choices=choices)
    else:
        form = PollForm(data=request.POST)
        form.fields["choice"] = forms.ChoiceField(choices=choices)
        if form.is_valid():
            # use form results
            chosen = form.cleaned_data["choice"]
            poll.values[request.user.username] = int(chosen)
            poll.save()
            print(*poll.values.values())
            return redirect('mainpage:viewpoll', poll_id)
    context = {'form' : form, 'poll' : poll}
    return render(request, 'mainpage/pollform.html', context)

@login_required
def viewpoll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    total = len(poll.values) - 1
    vals = []
    for choice in poll.choices:
        vals.append([choice, 0, 0])
    for val in poll.values.values():
        if val != -1:
            vals[val][1] += 1
            vals[val][2] = vals[val][1] / total * 100
    context = {"poll":poll, "total":total, "values":vals}
    return render(request, "mainpage/viewp.html", context)

@login_required
def newtopic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainpage:discuss')
    context = {'form':form}
    return render(request, 'mainpage/newtopic.html', context)