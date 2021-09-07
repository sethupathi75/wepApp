from django.db import models

# Create your models here.
class computerstore(models.Model):
    Product_name=models.CharField(max_length=20)
    Description=models.CharField(max_length=5000)
    image=models.FileField(upload_to='images/')