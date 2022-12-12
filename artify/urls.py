from django.urls import path
from . import views
from django.urls import path, include
from django.http import HttpResponse
from artify.views import PostList

urlpatterns = [
    #path("", views.home_page, name="Posts"),
    path("",PostList.as_view(), name="list"),
    #Below link to test sub paths in django
    path("test/", views.test, name="test"),
    ]