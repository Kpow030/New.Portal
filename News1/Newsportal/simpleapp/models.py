from django.db import models
from django.shortcuts import  reverse




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(
        max_length=100)
    Text = models.TextField(null=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.title)




# Create your models here.




