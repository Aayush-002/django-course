from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"website/index.html")
    # return HttpResponse("You are at chai aur django homepage.")

def about(request):
    return HttpResponse("You are at chai aur django about.")

def contact(request):
    return HttpResponse("You are at chai aur django contact.")