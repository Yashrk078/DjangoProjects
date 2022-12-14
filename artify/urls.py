from django.urls import path
from . import views
from django.urls import path, include
from django.http import HttpResponse
from artify.views import PostList, PostCreateView
from artify.form import PostCreate

urlpatterns = [
    #path("", views.home_page, name="Posts"),
    path("",PostList.as_view(), name="list"),
    path('new/', PostCreateView.as_view(), name='new'),
    #Below link to test sub paths in django
    path("test/", views.test, name="test"),
    ]