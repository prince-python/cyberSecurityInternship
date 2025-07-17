from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("Welcome to the Web Vulnerability Scanner!")
