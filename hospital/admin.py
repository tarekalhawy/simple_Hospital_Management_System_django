from django.contrib import admin
from . models import Patient, Doctor, Appoinment

# Register your models here.
admin.site.register(Patient)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'special')

admin.site.register(Doctor, DoctorAdmin)

class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'time')
    
admin.site.register(Appoinment, AppoinmentAdmin)
