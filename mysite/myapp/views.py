from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

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
                    customer = form.cleaned_data.get('fname')
                    messages.success(request, 'Account was created for ' + customer)
                    return redirect('sign')
			

        context = {'form':form}
        return render (request, 'myapp/registration.html', context)



def main(request):
    return render(request,"myapp/Main.html")


def about(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "myapp/course.html")

def contacts(request):
    return render(request, 'myapp/contacts.html')

def catalog(request):
    return render(request, 'myapp/catalog.html')

def sign(request):
    return render(request,'myapp/sign.html')

def register(request):
    return render(request,'myapp/registration.html')
