from django import forms
from .models import * 
from django.views.generic.edit import CreateView

class PostCreate(CreateView):
    model = Posts
    fields = ['image','description']
#,'author' should be included in the list, but its giving Integrity Errors
    success_url='/artify/'
    
