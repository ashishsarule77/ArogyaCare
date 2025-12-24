from django.shortcuts import render
from core.models import contactModel,Appointment,subscribefooter,singleblogModel
from django.http import HttpResponse


# Create your views here.


def view_home(request):
    resp = render(request,"core/home.html")
    return resp


def view_about(request):
    resp = render(request,"core/about.html")
    return resp


def view_service(request):
    resp = render(request,"core/service.html")
    return resp

def view_department(request):
    resp = render(request,"core/department.html")   
    return resp 


def view_single_department(requst):
    resp = render(requst,"core/single_department.html")
    return resp


def view_doctor(request):
    resp = render(request,"core/doctor.html")
    return resp

def view_singledoctor(request):
    resp = render(request,"core/single_doctor.html")
    return resp


def view_blog_sidebar(request):
    resp = render(request,"core/blog.html") 
    return resp 

def view_single_blog(request):
    resp = render(request,"core/single_blog.html")
    return resp


def view_contact(request):
    if request.method == "POST":
        contact = contactModel.objects.create(
            name =request.POST.get("name",""),
            email =request.POST.get("email",""),
            subject =request.POST.get("subject",""),
            phoneNo =request.POST.get("phone",""),
            message =request.POST.get("message",""),
        )
        return render(request,"core/contactsuccessful.html",{"name":contact.name})
    
    return render(request,"core/contact.html")

def view_appoinment(request):
    if request.method =="POST":
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        appointment_date = request.POST.get("date")
        appointment_time = request.POST.get("time")
        full_name = request.POST.get("name")
        phone_number = request.POST.get("phone")
        message = request.POST.get("message")

        Appointment.objects.create(
            department=department,
            doctor= doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            full_name=full_name,
            phone_number=phone_number,
            message=message

            
        )
        return render(request,"core/appoinment_successfull.html")
    return render(request,"core/appoinment.html")


def view_subscribefooter(request):
    if request.method =="POST":
        subscribe= subscribefooter.objects.create(
            email=request.POST.get("email","")
        )
        return render(request,"core/emailsuccessfull.html",{"emailname":subscribe.email})

# single blog page
def view_singleblog(request):
    if request.method =="POST":
        blog =singleblogModel.objects.create(
            name=request.POST.get("name",""),
            email=request.POST.get("email",""),
            message=request.POST.get("message","")
        )
        return render(request,"core/singleblogsuccessfull.html",{"blogname":blog.name})