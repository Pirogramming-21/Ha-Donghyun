from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    login_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='write_posts')
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    like_users = models.ManyToManyField(User, null=True, related_name='like_posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='write_comments')
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='related_post')
    content = models.TextField()
    like_users = models.ManyToManyField(User, null=True, related_name='like_comments')
    created_at = models.DateTimeField(auto_now_add=True)