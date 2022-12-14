from django.shortcuts import render, redirect
from artify.models import Posts, Post
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .form import * 


def home_page(request):
    posts = Posts.objects.all()
    #context = {"posts" : posts}
    return render(request, 'artify/artify.html')
def test(request):
    return HttpResponse("Hehe")

class PostList(ListView):
    model = Post
    template_name='artify/posts_list.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['image', 'description','author']
    template_name = 'artify/posts_form.html'
    success_url='/artify/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def uploadPost(request):
    if request.method== "POST":
        form = Post(request.POST, request.FILES)
        if form.is_valid(form):
            form.save()
            return redirect('list')
    else:
        form = Post()
    return render(request, 'artify/post_form.html', {'form': form})

