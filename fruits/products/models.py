from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    is_available = models.BooleanField(default=True)

