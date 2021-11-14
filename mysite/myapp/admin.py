from django.contrib import admin
from .models import Company, Vehicle, Customer, ContactForm, Rental


class CompanyAdmin(admin.ModelAdmin):
    pass


class VehicleAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


class RentalAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(ContactForm, ContactAdmin)