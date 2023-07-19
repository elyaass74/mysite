from django.contrib import admin
from website.models import contact


class contactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    #fields=('title',)
    list_display = ('name','subject' ,'created_date')
    list_filter = ('email',)
    #ordering=['created_date']
    search_fields=['name' , 'email']




admin.site.register(contact,contactAdmin)
