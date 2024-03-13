from django.db import models
from django.shortcuts import  reverse

class Post(models.Model):
    title = models.CharField(
        max_length=100)
    Text = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)



# Create your models here.


