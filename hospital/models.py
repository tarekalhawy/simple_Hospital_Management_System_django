from django.db import models

# Create your models here.

class Doctor(models.Model):

    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Patient(models.Model):
    
    gender = [
        ('man','man'),
        ('woman', 'woman'),
    ]

    name = models.CharField(max_length=50)
    gender = models.CharField(choices=gender, max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appoinment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)   
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return str(self.patient)