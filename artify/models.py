from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=14)
    description = models.TextField(max_length=120)
    image = models.ImageField()
    #Create author, which when deleted, the posts will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    #tags = models.(max_length=14)
    #Add timestamp
    created = models.DateTimeField(auto_created=True)
    modified=models.DateTimeField(auto_created=True)

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_created=True)
    modified=models.DateTimeField(auto_created=True)