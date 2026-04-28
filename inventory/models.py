from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    price = models.FloatField(max_length=10)
    stock = models.PositiveIntegerField(max_length=10)
    created_at = models.DateTimeField(max_length=20, auto_now_add= True)
    updated_at = models.DateTimeField(max_length=20, auto_now= True)

    class Meta:
        verbose_name = 'Producto'

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
 
