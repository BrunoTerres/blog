from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # users