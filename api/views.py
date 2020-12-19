from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def IndexPage(request):
    tableData = PriceData.objects.all()
    imageData = ImageDataForIntro.objects.all()
    return render(request, "index.html", {'tableData': tableData, 'imageData': imageData})

def FormForMobile(request):
    if (request.method == "GET"):
        form = SubscribeForm()
        return render(request, 'form.html', {'form': form})
    else:
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')