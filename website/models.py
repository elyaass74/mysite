from django.db import models

# Create your models here.
class contact(models.Model):

    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject=models.CharField(max_length=255)
    text= models.TextField()
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_date']
        verbose_name='کاربر'
        verbose_name_plural='کاربرها'

    def __str__(self):
        return self.name 


