from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=14)
    description = models.TextField(max_length=120)
    image = models.ImageField(upload_to='uploads/')
    #Create author, which when deleted, the posts will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    #tags = models.(max_length=14)
    #Add timestamp
    created = models.DateTimeField(auto_created=True)
    modified=models.DateTimeField(auto_created=True)

class Post(models.Model):
     description=models.TextField(max_length=150)
     image=models.ImageField(upload_to='uploads/')
     author=models.ForeignKey(User, on_delete=models.CASCADE,null=True) 

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    text = models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_created=True)
    modified=models.DateTimeField(auto_created=True)