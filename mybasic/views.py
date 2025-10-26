from http.client import HTTPResponse
from django.shortcuts import render  # type: ignore

# Create your views here.

def home(request):
    return HTTPResponse('Hello world')