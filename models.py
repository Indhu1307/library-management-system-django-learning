from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200) #charfield -shorttext store
    category=models.CharField(max_length=100)  

    description=models.TextField()  # long text store
    price=models.DecimalField(max_digits=8,decimal_places=2)

    image_url=models.URLField(blank=True) #option


    def __str__(self):
        return self.title
