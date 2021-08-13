from django.db import models

from post.models import Post
from user.models import User


class Commentary(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
