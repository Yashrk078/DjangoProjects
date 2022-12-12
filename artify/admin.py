from django.contrib import admin
from artify.models import Posts
# Register your models here.

admin.site.register(Posts, admin.ModelAdmin)