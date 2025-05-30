from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servicemaster(models.Model):
    name=models.CharField(max_length=70,null=True, blank=True)
    age=models.IntegerField(null=True,blank=True)
    man_img=models.ImageField(upload_to='static/images')
    experiecer=models.CharField(max_length=70,null=True, blank=True)
    profession=models.CharField(max_length=70,null=True, blank=True)
    locality=models.CharField(max_length=70,null=True, blank=True)
    ratings=models.CharField(max_length=70,null=True, blank=True)
    
   
class Serviceaddmaster(models.Model):
    fname= models.CharField(max_length=70,null=True, blank=True)
    lname= models.CharField(max_length=70,null=True, blank=True)
    address= models.CharField(max_length=70,null=True, blank=True)
    phone= models.CharField(max_length=70,null=True, blank=True)
    amount= models.CharField(max_length=70,null=True, blank=True)
    #agent= models.CharField(max_length=70,null=True, blank=True)
    service= models.CharField(max_length=70,null=True, blank=True)
    servicename= models.CharField(max_length=70,null=True, blank=True)
    city= models.CharField(max_length=70,null=True, blank=True)
    pincode= models.CharField(max_length=70,null=True, blank=True)
    created_by =models.IntegerField()
    
    
    
   
   