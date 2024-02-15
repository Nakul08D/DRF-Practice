from django.db import models

# Create your models here.


class Employee(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    post=models.CharField(max_length=50)
    income=models.IntegerField()
    
    def __str__(self):
        return self.name
    