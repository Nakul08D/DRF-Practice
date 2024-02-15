from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    tittle=models.CharField(max_length=50)
    page=models.IntegerField()
    price=models.IntegerField()
    author=models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.tittle
    