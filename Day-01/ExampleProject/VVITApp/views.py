from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
	return HttpResponse("Welcome to APSSDC Workshop")

def greet(sd,n):
	return HttpResponse(f"Hi Welcome {n}")