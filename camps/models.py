from django.db import models

class Camp(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    activities = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    age_group = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    spots_available = models.IntegerField(null=True, blank=True)
