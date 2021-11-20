from django.urls import path
from . import views

from .views import send_gmail

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('send_mail/', send_gmail, name="send_mail"),
    path('sign/', views.loginPage, name='sign'),
    path('registration/', views.registerPage, name='registration'),
    path('logout/',views.logoutUser,name = 'logout')
]