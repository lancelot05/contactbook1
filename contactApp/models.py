from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
