from django.shortcuts import render
from artify.models import Posts
from django.http import HttpResponse
from django.views.generic.list import ListView

def home_page(request):
    posts = Posts.objects.all()
    #context = {"posts" : posts}
    return render(request, 'artify/artify.html')
def test(request):
    return HttpResponse("Hehe")

class PostList(ListView):
    model = Posts
