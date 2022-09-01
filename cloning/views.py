from textwrap import dedent
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'cloning/index.html')

def contact(request):
    return HttpResponse("This is my contactpage")

def about(request):
    return HttpResponse("This is my about page")

def privacy(request):
    return HttpResponse("This is my privacy page")

def disclaimer(request):
    return HttpResponse("This is my disclaimer page")