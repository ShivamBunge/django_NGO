from django.db import models
from django.db.models.expressions import F

# Create your models here.
class Donate(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    