from django.core import paginator
from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from .forms import CommentForm
from django.http import HttpResponseRedirect
from  .models import Post
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj':page_obj

    }
    return render (request,'blog/index.html',context)

def blog_details(request, slug):
    posts = Post.objects.get(slug=slug)
    similar_post = posts.tags.similar_objects()[:1]
    comments = posts.comment.all()

    if request.method == 'POST':
        comment_from = CommentForm(request.POST)
        if comment_from.is_valid():
            new_comment = comment_from.save(commit=False)
            new_comment.posts=posts
            new_comment.save()
            #redirect to a new URL:
        messages.success(request,'Your comment submited.')
        return HttpResponseRedirect (request.path_info)


    #if a Get (or any other method) we'll create a blank from

    else:
        comment_from=CommentForm ()

    context = {
        'posts':posts,
        'similar_post':similar_post,
        'comments':comments,
        
    }
    return render (request,'blog/details.html',context)    

def search_blog (request):
    querySet = Post.objects.all()
    query = request. GET.get('q')

    paginator = Paginator (querySet,1)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(page_number)

    if query:
        querySet = querySet.filter(
            Q(title_icontains=querySet) | Q (short_description_icontains=query) |
            Q(description_icontains=query)
        ).distinct()

        context = {
            'queryset': querySet,
            'query': query
        }

        return render (request,'blog/search.html',context)