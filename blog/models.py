from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    #tag
    #image
    #category
    #author
    created_date = models.DateTimeField(auto_now_add=True)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    updated_date =models.DateTimeField(auto_now=True) 
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering=['-created_date']
        verbose_name='پست'
        verbose_name_plural='پست ها'

    def __str__(self):
        return ' {} - {} '.format(self.title,self.id)
    
  
