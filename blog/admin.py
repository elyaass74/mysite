from django.contrib import admin
from blog.models import Post,Category


class PostAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields=('title',)
    list_display = ('title','counted_view' , 'status' ,'created_date', 'published_date','author')
    list_filter = ('status','author')
    #ordering=['created_date']
    search_fields=['title' , 'author']

admin.site.register(Category)    

admin.site.register(Post,PostAdmin)