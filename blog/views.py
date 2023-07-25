from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from blog.models import Post

# Create your views here.
def blog_detail(request,pid):
    posts=Post.objects.filter(status=1)
    post=get_object_or_404(posts,pk=pid)
    context={'post':post}
    return render(request ,'blog/blog-detail.html',context)
   
   
    

def blog_single(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request ,'blog/blog-single.html',context)
    

def test_view(request,pid):
    #post=Post.objects.get(id=pid)
    post=get_object_or_404(Post,pk=pid)
    context={'post':post}
    return render(request,'test.html',context)