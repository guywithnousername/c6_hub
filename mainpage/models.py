from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

class Poll(models.Model):
    question = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add=True)
    choices = models.JSONField()
    values = models.JSONField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    

class Topic(models.Model):
    title = models.CharField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(max_length = 500)
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
    
def addnotif(user, notif):
    if hasattr(user, "notification"):
        user.notification.unread.insert(0, notif)
        user.notification.read = False
        user.notification.save()
    else:
        apps.get_model("users","Notification").objects.create(user=user,
        unread = [notif], read = False)