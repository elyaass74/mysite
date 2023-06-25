from django.shortcuts import render


# Create your views here.
def blog_detail(request):
    return render(request, 'blog/blog-detail.html' ) 

def blog_single(request):
    return render(request , 'blog/blog-single.html' )