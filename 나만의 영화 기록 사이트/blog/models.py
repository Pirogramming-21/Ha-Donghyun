from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=True, default="", max_length=200)
    released_date = models.CharField(null=True, default="", max_length=200)
    movieauthor = models.CharField(null=True, default="", max_length=200)
    actor = models.CharField(null=True, default="", max_length=200)
    genre = models.CharField(null=True, default="", max_length=200)
    rating = models.CharField(null=True, default="", max_length=200)
    running_time = models.CharField(null=True, default="", max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
