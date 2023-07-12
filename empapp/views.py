from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def home_view(request):
    return render(request,'empapp/home.html')