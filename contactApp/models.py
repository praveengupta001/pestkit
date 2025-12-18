from django.utils import timezone
from django.db import models

#create your models here.

class Contactform(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    # file upload fields
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    attachment = models.FileField(upload_to='uploads/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} <{self.email}>"

class Ourguards(models.Model):
    person = models.CharField(max_length=250)
    post = models.CharField(max_length=250)
    img = models.ImageField(upload_to='ourguards/', max_length=250, null=True, blank=True, default=None)

    def __str__(self):
        return self.person
