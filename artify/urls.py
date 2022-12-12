from django.urls import path
from . import views
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("", views.home_page, name="Posts"),
    #Below link to test sub paths in django
    path("test/", views.test, name="test")
    ]