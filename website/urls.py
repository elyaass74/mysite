
from django.urls import path
from website.views import *


urlpatterns = [
   
    #path('url','view','name')
    path('',index_view),
    path('about',about_view),
    path('contact' ,contact_view),
    
]