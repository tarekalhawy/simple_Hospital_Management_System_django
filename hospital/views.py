from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Doctor, Patient, Appoinment

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

 

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appoinment = Appoinment.objects.all()
    
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d += 1
    for i in patient:
        p += 1
    for i in appoinment:
        a += 1     
           
    context = {
        'd' : d,
        'p' : p,
        'a' : a
    }
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST' and 'btnin'in request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                messages.success(request, "Login Successfully")
            else:
                messages.error(request, 'Invalid Password or Username')
                # return redirect('login')
        else:
            messages.error(request, 'Invalid Password or Email')        
    return render(request, 'login.html')    

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Logout Successfully")
    return redirect('home')        

#------------------------------------------- 
#              doctor
# -------------------------------------------

def view_doctor(request):
    if request.user.is_authenticated:
        doctors = Doctor.objects.all()
        context = {
            'doctors' : doctors
        }
    else:
        return redirect('login')
    return render(request, 'view_doctor.html', context)


def delete_doctor(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            doctor = Doctor.objects.get(id=id)
            doctor.delete()
            messages.info(request, "Doctor Deleted Successfully")
            return redirect('view_doctor')
        
        

def add_doctor(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST' and 'btn_add_doctor'in request.POST:
                name = None
                mobile = None
                special = None
                
                if 'name' in request.POST: name = request.POST['name']
                else: messages.error('Error In Name')
                
                if 'mobile' in request.POST: mobile = request.POST['mobile']
                else: messages.error('Error In mobile')
                
                if 'special' in request.POST:special = request.POST['special']
                else: messages.error('Error In special')
                
                if name and mobile and special:
                    doctor = Doctor.objects.create(name=name, mobile=mobile, special=special)
                    messages.success(request, "Doctor Is Created Successfully")
                    return redirect('view_doctor')
                else:
                    messages.error(request, 'Invalid Value Check it') 
        else:
            return redirect('login')            
                            
    return render(request, 'add_doctor.html')     
    
#------------------------------------------- 
#              patient
# -------------------------------------------

def view_patient(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            patients = Patient.objects.all()
            context = {
                'patients' : patients
            }
        else:
            return redirect('login')
    return render(request, 'view_patient.html', context)


def delete_patient(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            patient = Patient.objects.get(id=id)
            patient.delete()
            messages.info(request, "Patient Deleted Successfully")
            return redirect('view_patient')
        
        

def add_patient(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST' and 'btn_add_patient'in request.POST:
                name = None
                gender = None
                mobile = None
                address = None
                
                if 'name' in request.POST: name= request.POST['name']
                else: messages.error('Error In Name')
                
                if 'gender' in request.POST: gender= request.POST['gender']
                else: messages.error('Error In Gender')
                
                if 'mobile' in request.POST: mobile= request.POST['mobile']
                else: messages.error('Error In Mobile')
                
                if 'address' in request.POST: address= request.POST['address']
                else: messages.error('Error In Address')
                
                if name and mobile and gender and address:
                    patient = Patient.objects.create(name=name, gender=gender, mobile=mobile, address=address)
                    messages.success(request, "Patient Is Created Successfully")
                    return redirect('view_patient')
                else:
                    messages.error(request, 'Invalid Value Check it') 
        else:
            return redirect('login')            
                            
    return render(request, 'add_patient.html')         

    
#------------------------------------------- 
#              Appoinment
# -------------------------------------------

def view_appoinment(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            appoinments = Appoinment.objects.all()
            context = {
                'appoinments' : appoinments
            }
        else:
            return redirect('login')
    return render(request, 'view_appoinment.html', context)


def delete_appoinment(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            appoinment = Appoinment.objects.get(id=id)
            appoinment.delete()
            messages.info(request, "Appoinment Deleted Successfully")
            return redirect('view_appoinment')

def add_appoinment(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST' and 'btn_add_appoinment'in request.POST:
                name_doctor = None
                name_patient = None
                date = None
                time = None
                
                if 'name_doctor' in request.POST: name_doctor= request.POST['name_doctor']
                else: messages.error('Error In name doctor')
                
                if 'name_patient' in request.POST: name_patient= request.POST['name_patient']
                else: messages.error('Error In name patient')
                
                if 'date' in request.POST: date= request.POST['date']
                else: messages.error('Error In date')
                
                if 'time' in request.POST: time= request.POST['time']
                else: messages.error('Error In time')
                
                if name_doctor and name_patient and date and time:
                    doctor = Doctor.objects.filter(name=name_doctor).first()
                    patient = Patient.objects.filter(name=name_patient).first()
                    
                    Appoinment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
                    messages.success(request, "Appoinment Is Created Successfully")
                    return redirect('view_appoinment')
                else:
                    messages.error(request, 'Invalid Value Check it') 
        else:
            return redirect('login') 
    context = {
        'doctors' : doctors,
        'patients' : patients
    }               
                            
    return render(request, 'add_appoinment.html', context)         