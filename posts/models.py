from django.db import models
from account.models import User


class Post(models.Model):
    user_id = models.ForeignKey("account.User", on_delete=models.CASCADE, db_column='user_id')
    title = models.CharField(max_length=500)
    body = models.TextField()
    summary = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)


class Report(models.Model):
    report_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE, db_column='post_id')
    user_id = models.ForeignKey("account.User", on_delete=models.CASCADE, db_column='user_id')