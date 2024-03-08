from django.contrib.auth.models import User
from django.db import models
from django.http import request

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Part(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True, default='product_images/default_image.jpg')
    model = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    power = models.CharField(max_length=255, blank=True, null=True)
    consumption = models.CharField(max_length=255, blank=True, null=True)
    transmission = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title