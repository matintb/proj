from django.urls import path
from website.views import *

# وقتی پروژه بزرگ باشه ممکنه اسمها شبیه باشه پس از اپ نیم استفاده کردیم ولی اگه تداخل نباشه لازم نیست
# بعد هم داخل تمپلت بیس {% url 'website:about' %}
# جنگو ۲ میتونیم به جای این داستان بریم داخل سستینگ و به اپ وبسایت رو اضافه کنیم

app_name = 'website'

urlpatterns = [
    # path(' url ',' view ')
    path('', index_view, name='index' ),
    path('about/', about_view, name='about' ),
    path('contact/', contact_view, name='contact' ),
    path('test/', test_view, name='test' ),
    path('newsletter/', newsletter_view, name='newsletter' )
    
]