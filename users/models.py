from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unread = models.JSONField(null=True)
    read = models.BooleanField(null=True)

class Points(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField()

def addnotif(user, notif):
    if hasattr(user, "notification"):
        user.notification.unread.insert(0, notif)
        user.notification.read = False
        user.notification.save()
    else:
        apps.get_model("users","Notification").objects.create(user=user,
        unread = [notif], read=False)

def addpoints(user, amount):
    if hasattr(user, "points"):
        user.points.points += amount
        user.points.save()
    else:
        apps.get_model("users", "Points").objects.create(user=user, points=amount)