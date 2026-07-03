from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse('<h1>Home page<h1/>')

def blog(request):
    return HttpResponse('<h1>Your blog<h1/>')

def about(request):
    return HttpResponse('<h1>About me<h1/>')