from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}: {self.username}"