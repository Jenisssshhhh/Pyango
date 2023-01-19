from django.db import models

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    Email = models.EmailField()
    Password = models.CharField(max_length=30)


    def __str__(self):
        return self.First_name

 