from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Answers(models.Model):
    questions = models.ForeignKey(
        Questions, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Likes(models.Model):
    answers = models.ForeignKey(
        Answers, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')
