from django.db import models

# Create your models here.
class contactModel(models.Model):
    name =models.CharField(max_length=20,blank=False,null=True)
    email =models.EmailField(null=True,blank=False,unique=False,)
    subject =models.CharField(max_length=100,blank=False,null=False)
    phoneNo =models.CharField(max_length=10,blank=False,null=False)
    message =models.TextField(blank=False,null=False)


    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    DEPARTMENT_CHOICE=[
        ('cardiology','cardiology'),
        ('neurology','neurology'),
        ('orthopedics','orthopedics'),
        ('pediatries','pediatries'),
        ('gynecology','gynecology'),
    ]

    DOCTOR_CHOICE=[
        ('dr_amit','dr. Amit Sharma'),
        ('dr_rahul','dr. rahul Verma'),
        ('dr_neha','dr. neha Singh'),
        ('dr_pooja','dr. Pooja Gupta'),
    ]

    department =models.CharField(max_length=50,choices=DEPARTMENT_CHOICE)
    doctor =models.CharField(max_length=50,choices=DOCTOR_CHOICE)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    full_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    message=models.TextField(blank=True,null=True)

    created_at =models.DateTimeField(auto_now_add=True)
    ia_active=models.BooleanField(default=True)


    def __str__(self):
        return f"{self.full_name} - {self.appointment_date}"


class subscribefooter(models.Model):
    email =models.EmailField(null=False,blank=False)


    def __str__(self):
        return self.email 
    

class singleblogModel(models.Model):
    name=models.CharField(max_length=25,null=False,blank=False)     
    email=models.EmailField(unique=True,null=False,blank=False)
    message=models.TextField(null=False,blank=False) 


    def __str__(self):
        return self.name    