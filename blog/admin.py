from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields=('title',)
    list_display = ('title','counted_view' , 'status' ,'created_date', 'published_date',)
    list_filter = ('status',)
    #ordering=['created_date']
    search_fields=['title' , 'content']

admin.site.register(Post,PostAdmin)