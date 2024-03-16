from django.shortcuts import render
from django.http import HttpResponse
from .services import search_books

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")
