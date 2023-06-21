from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index_view(request):
    return HttpResponse('<h1>Home page</h1>')
def about_view(request):
    return HttpResponse('<h1>About me</h1>')

def contact_view(request):
    return HttpResponse('<h1>Contact me</h1>')
# Create your views here.
