from django.urls import path
from . import views

from .views import book_vehicle, send_gmail

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('send_mail/',send_gmail, name="send_mail"),
    path('contact_result', views.contacts_res, name='contact_result'),
    path('sign/', views.login, name='sign'),
    path('registration/', views.register, name='registration'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('view_details/<int:pk>/',views.vehicle_details,name='vehicle_detail'),
    # path('book/',views.book_vehicle,name='book')
]