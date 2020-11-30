from django.db import models

# Create your models here.

class wash_basin(models.Model):

    brand_options = {
        ('Hindware', 'Hindware'),
        ('Jayna', 'Jayna'),
        ('Marc', 'Marc'),
        ('Local', 'Local')
    }

    item_name = models.CharField(max_length = 40, unique=True)
    brand = models.CharField(max_length = 40, choices = brand_options)
    image = models.ImageField(blank=True, null=True)
    color = models.CharField(max_length = 20)
    price = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
