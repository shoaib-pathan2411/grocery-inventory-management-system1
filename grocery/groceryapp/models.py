from django.db import models

# Create your models here.
class Grocery(models.Model):
    groceryitems = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()
