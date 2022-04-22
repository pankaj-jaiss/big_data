from pyexpat import model
from django.db import models

# Create your models here.
class Migration1(models.Model):
    source = models.CharField(max_length=100) 
    user = models.CharField(max_length=100) 
    passwd = models.CharField(max_length=100,blank=True,null=True) 
    host = models.CharField(max_length=100) 
    port = models.IntegerField(null=False,blank=False) 
    service_name = models.CharField(max_length=100) 
    
