from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1><center>Run machine</center></h1>')

def rohit(request):
    return HttpResponse('<h1><center>Hit man</center></h1>')