from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

## Product management ......
class pdt_reg_tbl(models.Model):
    pdtname=models.CharField(max_length=100)
    pdtimage=models.FileField(upload_to="media")
    pdtprice=models.CharField(max_length=100)
    pdttax=models.CharField(max_length=100)
    pdtquality=models.CharField(max_length=100)
    pdtstatus=models.CharField(max_length=100)

# # Supplier Registration .....
class supp_reg_table(models.Model):
    supName=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    payment=models.DecimalField(max_digits=9,decimal_places=2)