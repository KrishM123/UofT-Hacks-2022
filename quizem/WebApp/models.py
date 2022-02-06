from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    type = models.CharField(max_length=20, default="Default")
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}: {self.username}"

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    tage = models.CharField(max_length=1000)

class History(models.Model):
    user = Users
    question = Question
    correct = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)