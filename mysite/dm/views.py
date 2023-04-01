from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, 达梦数据库。 ")

# Create your views here.
