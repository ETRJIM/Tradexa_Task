from django.db import models

# Create your models here.

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    weight = models.DecimalField(max_digits=10,decimal_places=2,help_text=" Kgs")
    price = models.DecimalField(max_digits=10,decimal_places=2,help_text=" INR")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name