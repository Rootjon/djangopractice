from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/',views.blog_list, name='blog_list')

]