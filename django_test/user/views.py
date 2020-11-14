from . import views
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
	users = User.objects.all()
	return HttpResponse(F"{users[0]} and {users[1]}")

def  message_view(request):
	messages = Message.objects.all()

	return HttpResponse(messages[0])

def home_view(request):
	messages = Message.objects.all()
	users = User.objects.all()

	context = {
				"users":users,
				"messages":messages}

	return render(request,'user/htmll.html',context)		


def user_register(request):

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
				
		return redirect("home_view")

	form = UserCreationForm()

	content = {"form":form}

	return render(request,"user/register.html",content)