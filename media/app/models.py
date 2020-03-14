from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.
class TV(models.Model):
    tv_name= models.CharField(max_length=100)
    tv_cat= models.CharField(max_length=100)
    tv_link=models.CharField(max_length=300)
    tv_img=models.ImageField(default='logo.jpg', upload_to='tvlogo')
    favorite= models.ManyToManyField(User, related_name='favorite', blank=True)

    def __str__(self):
        return self.tv_name

    class Meta:
        ordering=('-tv_name',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.tv_img.path)
        if img.width> 300 or img.height> 300:
            img.thumbnail((300,300))
            img.save(self.tv_img.path)

    

class Radio(models.Model):
    radio_name= models.CharField(max_length=100)
    radio_cat= models.CharField(max_length=100)
    radio_link= models.CharField(max_length=300)
    radio_img= models.ImageField(upload_to='radiologo', default='logo.jpg')

    def __str__(self):
        return self.radio_name


    class Meta:
        ordering=('-radio_name',)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img= Image.open(self.radio_img.path)
        if img.width> 300 or img.height> 300:
            img.thumbnail((300,300))
            img.save(self.radio_img.path)