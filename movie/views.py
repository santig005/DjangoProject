from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Movie

def home(request):
    #return render(request, 'home.html',{'name':'Santiago Gomez'})
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html',{'searchTerm':searchTerm})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')