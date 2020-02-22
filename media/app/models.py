from django.db import models

# Create your models here.
class TV(models.Model):
    tv_name= models.CharField(max_length=100)
    tv_cat= models.CharField(max_length=100)
    tv_link=models.CharField(max_length=300)
    tv_img=models.ImageField(default='logo.jpg', upload_to='tvlogo')
