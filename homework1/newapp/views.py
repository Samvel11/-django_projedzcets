from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def start(request):
	return HttpResponse("This is the main page")

def hello(request):
	return HttpResponse("Hello django world")

def about(request):
	return HttpResponse("Page about us")
def time (request):
	t = datetime.now()
	return HttpResponse(f"Current date is {t}")

def square(request):
	d = {}
	for i in range(16):
		d[i] = i**2

	return HttpResponse(f"{d}")
