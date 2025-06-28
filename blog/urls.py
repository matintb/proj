from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    # path(' url ',' view ')
    path('', blog_home, name='home' ),
    # path('single/', blog_single, name='single' ),
    path('<int:pid>', blog_single, name='single' ),
    path('testblog/', test_blog, name='testblog' ),
    # path('post-<int:pid>', dynamictest, name='dynamictest' )
    # path('<str:name>/<str:family_name>/<int:age>', dynamictest, name='dynamictest' )
    # path('<str:name>/lastname/<str:family_name>/age/<int:age>', dynamictest, name='dynamictest' )

]