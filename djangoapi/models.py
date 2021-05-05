from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - ${self.price}'
