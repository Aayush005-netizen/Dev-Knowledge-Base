from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    return render(request, 'websites/index.html')
    #return HttpResponse("Hello, world! You are at my first ever Django home page.")

def about(request):
    return HttpResponse("Hello, world! You are at my first ever Django about page.")

def contact(request):
    return HttpResponse("Hello, world! You are at my first ever Django contact page.")

