from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title





class Quote(models.Model):
	author= models.CharField(max_length=80)
	quote= models.TextField()

	def __str__(self):
		return self.author




class Project(models.Model):
    name= models.CharField(max_length=200)
    git_repo= models.CharField(max_length=200)
    picture= models.FileField(null=True, blank=True)
    purpose= models.CharField(max_length=400)
    description= models.TextField()

    def __str__(self):
        return self.name