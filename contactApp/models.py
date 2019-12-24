from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class ContactInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='', null=True)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)


    def __str__(self):
        return self.name
