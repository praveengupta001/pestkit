from django.db import models

# Create your models here.
class Service(models.Model):
    service_title=models.CharField(max_length=150)
    service_desc=models.TextField()
    service_read_link=models.CharField(max_length=150)

class contactfrom(models.Model):
    fullname=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    message=models.CharField(max_length=250)