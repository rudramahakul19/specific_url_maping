from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def phillips(request):
    return HttpResponse('<h1><center>Best Wicketkeeper</center></h1>')

def williamson(request):
    return HttpResponse('<h1><center>current captain of the team in ODIs and T20Is</center></h1>')