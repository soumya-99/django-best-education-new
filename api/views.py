from django.shortcuts import render
from .models import *

# Create your views here.

def IndexPage(request):
    tableData = PriceData.objects.all()
    imageData = ImageDataForIntro.objects.all()
    return render(request, "index.html", {'tableData': tableData, 'imageData': imageData})

def FormForMobile(request):
    return render(request, "form.html")
