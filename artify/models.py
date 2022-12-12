from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=14)
    description = models.TextField(max_length=120)
    postImage = models.FilePathField(path="")
    #tags = models.(max_length=14)