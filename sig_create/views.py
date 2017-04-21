from django.shortcuts import render
from django.http import HttpResponse
#test

def index(request):
    return HttpResponse("Hello, world. You're at the sigs index.")
