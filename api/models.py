from django.db import models
from django import forms

# Create your models here.

class PriceData(models.Model):
    name = models.CharField("Name", max_length=250)
    subject = models.CharField("Subject", max_length=300)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class ImageDataForIntro(models.Model):
    image = models.ImageField(upload_to="carousel_images", blank=True)

class SubscriptionForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.email