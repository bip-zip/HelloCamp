from django.db import models
class Camp(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)  # Add the fax field
    activities = models.TextField(null=True, blank=True)
    cost = models.CharField(max_length=100, null=True, blank=True)
    age_group = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.CharField(max_length=100, null=True, blank=True)
    spots_available = models.IntegerField(default=10, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='camps/', null=True, blank=True)

