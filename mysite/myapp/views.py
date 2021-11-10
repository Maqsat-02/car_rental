from django.shortcuts import render
from django.http import HttpResponse

from django.template import Template, Context
import datetime


# Create your views here.

def team(request):
    now = datetime.datetime.now()

    person = {'firstname': 'BARBARA', 'lastname': 'MORI'}
    person2 = {'firstname': 'HARRY', 'lastname': 'DICKENS'}
    person3 = {'firstname': 'SAMMIE', 'lastname': 'LOUIS'}
    person4 = {'firstname': 'JOHN', 'lastname': 'WRIGHT'}
    project_name = "Car Rent"
    context = {
        'person': person,
        'person1': person2,
        'person2': person3,
        'person3': person4,
    }
    return render(request, 'myapp/team.html', context)


def contacts(request):
    person = {'name': 'Amangeldi Maksat', 'position': 'Developer', 'mail': 'amangeldymaksat7@gmail.com', 'phone': '87478046016',
              'office_h': '9:00-15-00'}
    person2 = {'name': 'Les Nurzhan', 'position': 'Team Leader', 'mail': 'nurzhan@gmail.com', 'phone': '87478035041',
               'office_h': '9:00-15-00'}

    context = {
        'person': person,
        'person1': person2,

    }
    return render(request, 'myapp/contacts.html', context)



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
