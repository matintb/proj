from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from website.forms import ContactForm,NewsletterForm

# Create your views here.

def http_res(request):
    return HttpResponse('http-res')

def json_res(request):
    return JsonResponse({'name':'ali'})

def index_view(request):
    return render(request,'website/index.html')

# return render(request,'با رندر به سراغ فایل تمپلیت رفت و از ان نام فایل را سرچ نمود')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def test_view(request):
    return render(request,'website/test.html',{'fname':'matin', 'lname':'tb'})

def newsletter_view(request):
        if request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return  HttpResponseRedirect('/')
        else:
                return  HttpResponseRedirect('/')