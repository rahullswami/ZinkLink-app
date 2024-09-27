from django.db import models
from django.utils import timezone
# Create your models here.

class Zink_user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    profile_bio = models.TextField()
    profile_link = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profile')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class News(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)
    news = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.heading


class Post(models.Model):
    post = models.ImageField(upload_to='user-post')
    fullname = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname

class Chat(models.Model):
    chat = models.TextField()
    created_at = models.DateTimeField(default=timezone.now) 