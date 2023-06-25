from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def blog_detail(request):
    context = {'title':'sajad new site is started' , 'content': 'thss site is foundated by elyas with django' , 'author':'elays'}
    return render(request, 'blog/blog-detail.html',context ) 

def blog_single(request):
    return render(request , 'blog/blog-single.html' )