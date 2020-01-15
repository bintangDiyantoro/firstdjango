from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def home2(request):
    return HttpResponse("<h1>Halo dunia</h1>")

def about(request):
    return HttpResponse("<h1>About page</h1>")