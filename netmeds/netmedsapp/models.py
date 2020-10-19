from django.db import models

# Create your models here.
class medicine_type(models.Model):
    medicine_genre = models.CharField(max_length=64)

class Medicines(models.Model):
    name = models.CharField(max_length=64)
    manufaturer = models.CharField(max_length=64)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    key_benifits = models.CharField(max_length=100)
    dosage = models.CharField(max_length=64)
    safety_info = models.CharField(max_length=100)
    other_info = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    genres = models.ManyToManyField(medicine_type, blank=True, null=True)

