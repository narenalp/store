from django.db import models


# Create your models here.

class UnitMaster(models.Model):
    unit = models.CharField(max_length=6)

class Items(models.Model):
    ItemCode = models.CharField(max_length=6)
    ItemName = models.CharField(max_length=30)
    ItemDesc = models.CharField(max_length=100)
    Type = models.CharField(max_length=10)
    Make = models.CharField(max_length=30)
    category = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(UnitMaster, on_delete=models.CASCADE)

