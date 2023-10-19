from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

class Part(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
