from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
   
    #path('url','view','name')
    path('<int:pid>',blog_detail , name='index'),
    path('single',blog_single,name='single'),
    #path('post-<int:pid>',test_view,name='test')
 
    
    
]