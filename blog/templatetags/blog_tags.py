from django import template
from blog.models import post


# must create a register obj to be valid
register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    posts = post.objects.filter(status=1).count()
    return posts
