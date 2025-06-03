from django.shortcuts import render


def blog_home(requests):
    return render(requests,'blog/blog-home.html')

def blog_single(requests):
    content = {'title':'bitcoin', 'text':'bitcoin is the best', 'writer':'great Matin'}
    return render(requests,'blog/blog-single.html',content)


