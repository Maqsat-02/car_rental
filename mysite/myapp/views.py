from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail

# Create your views here.
from .models import *
from .forms import  CreateUserForm
# from .filters import OrderFilter

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('main')
	
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                customer = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + customer)
                return redirect('sign')
			

    context = {'form':form}
    return render (request, 'myapp/registration.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('main')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('main')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'myapp/sign.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main')

def main(request):
    return render(request,"myapp/Main.html")


def about(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "myapp/course.html")

def contacts(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "myapp/contacts.html")

def send_gmail(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        print(name, email, subject, message)

        send_mail(
            subject,
            message,
            email,
            ['CRentalHelp@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect(('/contacts'))
    else:
        return HttpResponse('Invalid request')


@login_required(login_url='sign')
def catalog(request):
    return render(request, 'myapp/catalog.html')
