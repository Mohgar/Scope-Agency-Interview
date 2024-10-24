from django.db import models



class InvoiceDetails(models.Model):
    lineNo = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=100,)
    UnitNo = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    expiryDate = models.DateTimeField()


class Unit(models.Model):
    unitNo = models.IntegerField(primary_key=True)
    unitName = models.CharField(max_length=100)





# Create your models here.
