from django.db import models
import hashlib

from role.models import Role


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    #commentaries
    #posts

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.password = hashlib.md5(bytes(self.password, encoding='utf-8')).hexdigest()
        super().save(force_insert, force_update, using, update_fields)

