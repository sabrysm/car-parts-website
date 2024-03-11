from django.contrib.auth.models import User
from django.db import models
from django.http import request
from django.utils import timezone

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


    def sell_part(self):
        SaleHistory.objects.create(part=self, sold=True)
        self.quantity -= 1
        self.save()
    
    def add_quantity(self, quantity):
        self.quantity += quantity
        SaleHistory.objects.create(part=self, sold=False)
        self.save()

class SaleHistory(models.Model):
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    sold_at = models.DateTimeField(default=timezone.now)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.part.title} - sold at {self.sold_at}"