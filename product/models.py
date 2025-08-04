from django.db import models
from datetime import date

# Create your models here.
class prod_model(models.Model):
    id=models.AutoField(primary_key=True)
    Mobile= models.CharField(max_length=10,null=True)
    ProductName=models.CharField(max_length=100)
    price=models.IntegerField()
    Description=models.TextField()
    Product_stock=models.IntegerField(null=True)
    Image=models.FileField(null=True)
    date=models.DateField(default=date.today ,editable=False)
    status=models.IntegerField(default=1,editable=False)
    class Meta:
        db_table="Product_Details"