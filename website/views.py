from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index_view(request):
    return render(request , 'website/index.html')

def about_view(request):
    return render(request , 'website/about-us.html')

def contact_view(request):
    return render(request , 'website/contact-us.html')


