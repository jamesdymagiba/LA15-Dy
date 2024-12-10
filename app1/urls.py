from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
    path('hi/', views.say_hi, name='say_hi'),
    path('posts/', views.blog_list, name='blog_list'), 
    path('posts/<int:id>/', views.blog_detail, name='blog_detail'),  
]
