from django.db import models

# Create your models here.
class Grocery(models.Model):
    groceryitems = models.CharField(max_length=50)
    price = models.FloatField()
    Discounts = models.IntegerField()
    date = models.DateField()

class Discount(models.Model):
    discountpercentage = models.FloatField()
    Date = models.DateField(auto_now_add=True)

