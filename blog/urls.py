from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/',views.blog_list, name='blog_list'),
    path('blog/<slug>/',views.blog_details, name='blog_details'),
    path('search/',views.search_blog,name='search_blog')

]