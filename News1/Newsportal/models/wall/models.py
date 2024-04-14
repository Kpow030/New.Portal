from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email

class Post(models.Model):
    name = models.CharField(max_length= 300)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name + "/" + str(self.subscribers)