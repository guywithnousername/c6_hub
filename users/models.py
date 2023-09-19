from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

class Notification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unread = models.JSONField(null=True)

def addnotif(user, notif):
    if hasattr(user, "notification"):
        user.notification.unread.insert(0, notif)
        user.notification.save()
    else:
        apps.get_model("users","Notification").objects.create(user=user,
        unread = [notif])