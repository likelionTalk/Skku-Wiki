from django.contrib import admin
from .models import Post, Report, Like

# Register your models here.
admin.site.register(Post)
admin.site.register(Report)
admin.site.register(Like)