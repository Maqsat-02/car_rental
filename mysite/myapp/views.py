from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.template import Template, Context
import datetime

# Create your views here.
from .forms import UserForm, CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('sign')

        context = {'form': form}
        return render(request, 'myapp/registration.html', context)


def logoutUser(request):
    logout(request)
    return redirect('sign')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'myapp/sign.html', context)


def main(request):
    return render(request, "myapp/Main.html")


def about(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "myapp/course.html")


def contacts(request):
    return render(request, 'myapp/contacts.html')


@login_required(login_url='sign')
def catalog(request):
    return render(request, 'myapp/catalog.html')


# def sign(request):
#     userform = UserForm()
#     return render(request,'myapp/sign.html', {"form": userform})

def register(request):
    return render(request, 'myapp/registration.html')
