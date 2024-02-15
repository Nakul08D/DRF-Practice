from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    duration=models.IntegerField()
    discount=models.IntegerField()
    
    def __str__(self):
        return self.name
    
