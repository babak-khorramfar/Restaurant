from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog(request):
    blog_list = Blog.objects.all()
    context = {
        'blog' : blog_list
    }
    return render(request, 'blog/blog.html', context)


def post(request, id):
    post = Blog.objects.get(id=id)
    context = {
        'post' : post
    }

    return render(request, 'blog/post.html', context)