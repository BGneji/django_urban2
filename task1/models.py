from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=3)
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(200)
        ]
    )
    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    size = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
