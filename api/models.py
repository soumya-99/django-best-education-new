from django.db import models

# Create your models here.

class PriceData(models.Model):
    name = models.CharField("Name", max_length=250)
    subject = models.CharField("Subject", max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class ImageDataForIntro(models.Model):
    image = models.ImageField(upload_to="images", blank=True)