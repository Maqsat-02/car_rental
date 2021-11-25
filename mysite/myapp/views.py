from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from datetime import datetime, timedelta
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout

from .forms import RegistrationForm, LoginForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import *

# from .filters import OrderFilter
def register(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You already authenticated as {user.email}')

    context = {
        
    }

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            auth_login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('sign')
        else:
            context['registration_form'] = form

    return render(request, 'myapp/registration.html', context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get("next"))
    return redirect

def login(request, *args, **kwargs):
    context = {
       
    }

    user = request.user
    if user.is_authenticated:
        return redirect('main')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                auth_login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('main')
            else:
                context['login_form'] = form

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
def contacts_res(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "myapp/contact_result.html")
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

        return HttpResponseRedirect(('/contact_result'))
    else:
        return HttpResponse('Invalid request')



def catalog(request):
    vehicles = Vehicle.objects.all
    user = User.objects.all
    context = {
        'user': user,
        'vehicles': vehicles
    }

    return render(request, 'myapp/catalog.html',context)

def vehicle_details(request, pk):
    vehicle = get_object_or_404(Vehicle, pk = pk)
    # vehicle = Vehicle.objects.get(id=pk)
    context = {
        'vehicle': vehicle
    }
    return render(request, 'myapp/details.html', context)

def book_vehicle(request,**kwargs):
    vehicle = get_object_or_404(Vehicle, pk = kwargs.get('pk_v'))
    user = get_object_or_404(User, pk = kwargs.get('pk_u'))
    rental = Rental.objects.create(date_out=datetime.now(),date_return=datetime.now() + timedelta(hours=24),day_cost=vehicle.per_day,vehicle=vehicle,Customer=user)
    rental.save()
    context = {
        'rental': rental
    }
    return render(request,'myapp/book.html',context)
