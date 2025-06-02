from django.urls import path
from website.views import index_view,about_view,contact_view

# وقتی پروژه بزرگ باشه ممکنه اسمها شبیه باشه پس از اپ نیم استفاده کردیم ولی اگه تداخل نباشه لازم نیست
# بعد هم داخل تمپلت بیس {% url 'website:about' %}
# جنگو ۲ میتونیم به جای این داستان بریم داخل سستینگ و به اپ وبسایت رو اضافه کنیم

app_name = 'website'

urlpatterns = [
    # path(' url ',' view ')
    path('', index_view, name='index' ),
    path('about/', about_view, name='about' ),
    path('contact/', contact_view, name='contact' )
]