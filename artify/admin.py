from django.contrib import admin
from artify.models import Post
# Register your models here.

admin.site.register(Post, admin.ModelAdmin)