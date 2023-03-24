
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('admin_login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('index/',views.index, name='dashboard'),
    #  doctor
    path('view_doctor/',views.view_doctor, name='view_doctor'),
    path('delete_doctor<int:id>/',views.delete_doctor, name='delete_doctor'),
    path('add_doctor/',views.add_doctor, name='add_doctor'),
    # patient
    path('view_patient/',views.view_patient, name='view_patient'),
    path('delete_patient<int:id>/',views.delete_patient, name='delete_patient'),
    path('add_patient/',views.add_patient, name='add_patient'),
    # appoinment
    path('view_appoinment/',views.view_appoinment, name='view_appoinment'),
    path('delete_appoinment<int:id>/',views.delete_appoinment, name='delete_appoinment'),
    path('add_appoinment/',views.add_appoinment, name='add_appoinment'),
]
