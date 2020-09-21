from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.db import models


class Novel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='novels')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-id',)


class Chapter(models.Model):
    novel = models.ForeignKey(Novel,
                              on_delete=models.CASCADE,
                              related_name='chapters')
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
