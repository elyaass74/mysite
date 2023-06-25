from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
   
    #path('url','view','name')
    path('',blog_detail , name='index'),
    path('single',blog_single,name='single'),
 
    
    
]