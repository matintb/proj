from django.shortcuts import render,get_object_or_404
from blog.models import post

def blog_home(requests,**kwargs):
    # posts = post.objects.all()
    posts = post.objects.filter(status=1)
    # if not len(kwargs)>0:
    #     pass
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name']) 
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts':posts}
    return render(requests,'blog/blog-home.html',context)

# def blog_category(requests,cat_name):
#     posts = post.objects.filter(status=1)
#     # looks for name __name insted of id
#     posts = posts.filter(category__name=cat_name)  
#     context = {'posts':posts}
#     return render(requests,'blog/blog-home.html',context)

# def blog_single(requests):
#     content = {'title':'bitcoin', 'text':'bitcoin is the best', 'writer':'great Matin'}
#     return render(requests,'blog/blog-single.html',content)

def blog_single(requests,pid):
    # filter kardim ta karbar be sorat dasti natone be post hay publish nashode dast peyda kone
    posts = post.objects.filter(status=1)
    mypost = get_object_or_404(posts,pk=pid)
    # mypost = post.objects.get(id=pid)
    context = {'mypost':mypost}
    return render(requests,'blog/blog-single.html',context)

def test_blog(requests):
    posts = post.objects.all()
    # posts = post.objects.filter(satus=1)
    context = {'posts':posts}
    return render(requests,'blog/testblog.html',context)


# def dynamictest(requests,name,family_name,age):   
#     context = {'name':name,'family_name':family_name,'age':age}
#     return render(requests,'blog/dynamictest.html',context)

def dynamictest(requests,pid): 
    posts = post.objects.all()
    # mypost = post.objects.get(id=pid)
    # pk : primary key
    mypost = get_object_or_404(post,pk=pid)
    context = {'pid':pid, 'posts':posts,'mypost':mypost}
    return render(requests,'blog/dynamictest.html',context)
