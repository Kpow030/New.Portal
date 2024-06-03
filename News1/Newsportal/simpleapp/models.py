from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.shortcuts import reverse

from Newsportal.models.models import Author


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'product-{self.pk}')


class Message(models.Model): # Модель отправки сообщений
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='sent_message')
    recipient = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='received_message')

    def __str__(self):
        return f'{self.sender.name} to {self.recipient.name}: {self.text[:50]}'


class File(models.Model): # Модель добавления в сообщения фалов
    file = models.FileField(upload_to='files/')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return f'{self.file.name} in {self.message.text[:50]}'




# Create your models here.




