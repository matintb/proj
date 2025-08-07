from django import template
from blog.models import post,Category,comments


# must create a register obj to be valid
register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    posts = post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='comments_count')
def comments_count(pid):
    if not pid:
        return 0
    try:
        return comments.objects.filter(Post=pid, approved=True).count()
    except post.DoesNotExist:
        return 0


@register.filter
def snippet(value,arg=15):
    return value[:arg] + ' ...'

@register.inclusion_tag('popularposts.html')
def popularposts():
    posts = post.objects.filter(status=1).order_by('-published_date')[:1]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}