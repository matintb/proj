from django.urls import path
from blog.views import *

from blog.feeds import LatestEntriesFeed


app_name = 'blog'

urlpatterns = [
    # path(' url ',' view ')
    path('', blog_home, name='home' ),
    # path('single/', blog_single, name='single' ),
    path('<int:pid>', blog_single, name='single' ),
    path('category/<str:cat_name>', blog_home, name='category' ),
    path('author/<str:author_username>', blog_home, name='author' ),
    path('tag/<str:tag_name>', blog_home, name='tag' ),
    path('search/', blog_search, name='search' ),
    path('testblog/', test_blog, name='testblog' ),
    path("rss/feed/", LatestEntriesFeed()),
    path('testform/', test_form, name='testform' ),
    # path('post-<int:pid>', dynamictest, name='dynamictest' )
    # path('<str:name>/<str:family_name>/<int:age>', dynamictest, name='dynamictest' )
    # path('<str:name>/lastname/<str:family_name>/age/<int:age>', dynamictest, name='dynamictest' )

]