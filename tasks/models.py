from django.db import models

class Tasks(models.Model):
    STATUS = [
        ('P' , 'pending'),
        ('I' , 'in progress'),
        ('C' , 'completed'),
    ]
    PRIORITY = [
        ('L' , 'low'),
        ('R' , 'regular'),
        ('H' , 'high'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    status = models.CharField(max_length=1, choices = STATUS)
    priority = models.CharField(max_length=1, choices = PRIORITY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
