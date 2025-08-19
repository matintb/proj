# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from blog.models import post, comments
from website.models import contact
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from website.forms import NameForm,ContactForm
from blog.forms import CommentForm
from taggit.models import Tag
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# @login_required
def blog_home(request,**kwargs):
    # posts = post.objects.all()
    posts = post.objects.filter(status=1)
    # if not len(kwargs)>0:
    #     pass
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name']) 
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    # paginator ( input , 3 = count of posts in one page   ) 
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    tags = Tag.objects.all()
    context = {'posts':posts, 'tags':tags}
    return render(request,'blog/blog-home.html',context)

# def blog_category(request,cat_name):
#     posts = post.objects.filter(status=1)
#     # looks for name __name insted of id
#     posts = posts.filter(category__name=cat_name)  
#     context = {'posts':posts}
#     return render(request,'blog/blog-home.html',context)

# def blog_single(request):
#     content = {'title':'bitcoin', 'text':'bitcoin is the best', 'writer':'great Matin'}
#     return render(request,'blog/blog-single.html',content)

def blog_single(request,pid):
    if request.method == "POST": 
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'succed')
        else:
            messages.add_message(request,messages.ERROR,'error')
    # filter kardim ta karbar be sorat dasti natone be post hay publish nashode dast peyda kone
    posts = post.objects.filter(status=1)
    mypost = get_object_or_404(posts,pk=pid)
    # mypost = post.objects.get(id=pid)
    if not mypost.login_require:
        comment = comments.objects.filter(Post=mypost.id,approved=True).order_by('-created_date')
        form = CommentForm()
        context = {'mypost':mypost,'comment':comment, 'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def test_blog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = contact()
        c.Name = name 
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
        
        print(name,email,subject,message)
    if request.method == 'GET':
        print("GET")
        
    posts = post.objects.all()
    # posts = post.objects.filter(satus=1)
    context = {'posts':posts}
    return render(request,'blog/testblog.html',context)


# def dynamictest(request,name,family_name,age):   
#     context = {'name':name,'family_name':family_name,'age':age}
#     return render(request,'blog/dynamictest.html',context)

def dynamictest(request,pid): 
    posts = post.objects.all()
    # mypost = post.objects.get(id=pid)
    # pk : primary key
    mypost = get_object_or_404(post,pk=pid)
    context = {'pid':pid, 'posts':posts,'mypost':mypost}
    return render(request,'blog/dynamictest.html',context)

def blog_search(request):
    # request.__dict__ -> shows objects in request
    # print(request.__dict__)
    posts = post.objects.filter(status=1)    
    if request.method == 'GET':
        # print('get request')
        # s:= -> if there is a s print it in s
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
        
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def test_form(request):
    if request.method == 'POST':
        # form = NameForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['Name']
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # c = contact()
            # c.Name = name 
            # c.email = email
            # c.subject = subject
            # c.message = message
            # c.save()
            # instead of all lines above just one line does the job
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
        
    # form = NameForm()
    form = ContactForm()
    return render(request,'blog/testform.html', {'form':form})

