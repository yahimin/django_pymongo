from django.db import models

# Create your models here.

class SampleDetails(models.Model):
    medicine_id=models.CharField(max_length=30)
    common_name = models.CharField(max_length=30)
    scientific_name = models.CharField(max_length=30)
    available = models.CharField(max_length=2)
    category = models.CharField(max_length=7)
    
