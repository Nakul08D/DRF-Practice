from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    number=models.IntegerField()
    email=models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
    
