from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self) -> str:
        return self.name
