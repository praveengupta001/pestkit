from django.db import models

class Ourguards(models.Model):
    person = models.CharField(max_length=250)
    post = models.CharField(max_length=250)
    img = models.ImageField(upload_to='ourguards/', max_length=250, null=True, blank=True, default=None)

    def __str__(self):
        return self.person
