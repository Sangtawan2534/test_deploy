from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<str:slug>', views.blog_detail, name="blog-details"),
    path('search', views.search, name="search"),
    path('contact', views.contact, name="contact")
]
