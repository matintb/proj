from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def http_res(requests):
    return HttpResponse('http-res')

def json_res(requests):
    return JsonResponse({'name':'ali'})

def index_view(requests):
    return render(requests,'website/index.html')

# return render(requests,'با رندر به سراغ فایل تمپلیت رفت و از ان نام فایل را سرچ نمود')

def about_view(requests):
    return render(requests,'website/about.html')

def contact_view(requests):
    return render(requests,'website/contact.html')

