from django.shortcuts import render
from blog.models import post

def blog_home(requests):
    # posts = post.objects.all()
    posts = post.objects.filter(status=1)
    context = {'posts':posts}
    return render(requests,'blog/blog-home.html',context)

def blog_single(requests):
    content = {'title':'bitcoin', 'text':'bitcoin is the best', 'writer':'great Matin'}
    return render(requests,'blog/blog-single.html',content)

def test_blog(requests):
    posts = post.objects.all()
    # posts = post.objects.filter(satus=1)
    context = {'posts':posts}
    return render(requests,'blog/testblog.html',context)
