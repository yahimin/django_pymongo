from django.db import models

# Create your models here.

# model 사용할때는 항상 장고는 마이그레이션을 진행하고 개발 서버 실행해야 적용
class SampleDetails(models.Model):
    medicine_id=models.CharField(max_length=30)
    common_name = models.CharField(max_length=30)
    scientific_name = models.CharField(max_length=30)
    available = models.CharField(max_length=2)
    category = models.CharField(max_length=7)
    
