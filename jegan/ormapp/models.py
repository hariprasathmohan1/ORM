from django.db import models
from django.contrib import admin
class ZomatoDB(models.Model):
    Address=models.CharField(max_length=10)
    Name=models.CharField(max_length=10)
    Coupon=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Bill=models.IntegerField()
    Upi_id=models.CharField(max_length=100)
    Mobile_no=models.IntegerField(primary_key=True)
class ZomatoDBAdmin(admin.ModelAdmin):
	list_display=['Address','Name','Coupon','Bill','Email','Upi_id','Mobile_no'];



