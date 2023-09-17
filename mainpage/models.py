from django.db import models
from django.contrib.auth.models import User

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
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(max_length = 500)
    date_added = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text