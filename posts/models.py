from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    summary = models.CharField(max_length=200, default="")
    date = models.DateTimeField(auto_now_add=True)
    