from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "exchange_rate/index_exchange.html")

def about(request):
    return render(request, "exchange_rate/about.html")