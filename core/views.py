from django.shortcuts import render
from core.models import contactModel,Appointment,subscribefooter,singleblogModel
from django.http import HttpResponse
from datetime import datetime,date


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

# def view_appoinment(request):
#     if request.method =="POST":
#         department = request.POST.get("department")
#         doctor = request.POST.get("doctor")
#         appointment_date = request.POST.get("date")
#         appointment_time = request.POST.get("time")
#         full_name = request.POST.get("name")
#         phone_number = request.POST.get("phone")
#         message = request.POST.get("message")

        # Appointment.objects.create(
        #     department=department,
        #     doctor= doctor,
        #     appointment_date=appointment_date,
        #     appointment_time=appointment_time,
        #     full_name=full_name,
        #     phone_number=phone_number,
        #     message=message

            
#         )


def view_appoinment(request):
    if request.method =="POST":
        department = request.POST.get("department","").strip()
        doctor = request.POST.get("doctor","").strip()
        appointment_date = request.POST.get("date","").strip()
        appointment_time = request.POST.get("time","").strip()
        full_name = request.POST.get("name","").strip()
        phone_number = request.POST.get("phone","").strip()
        message = request.POST.get("message","").strip()
        # validation error list
        errors =[]

        # validation department
        if not department or department == "Choose Department":
            errors.append("Please select a department") 

        # Valodate doctor
        if not doctor or doctor == "Select Doctors":
            errors.append(" Please select a doctor")

        if not appointment_date:
            errors.append("please select an appoinment date")
        else:
            try:
                date_obj =datetime.strptime(appointment_date,"%Y-%m-%d").date()
                if date_obj < date.today():
                    errors.append("appointment date can not be in the past") 
            except ValueError:
                errors.append("Invalide date format")             

        # validation appointment data
        if not appointment_time:
            errors.append("Please select appointment time")

        # validate full name  
        if not full_name:
            errors.append("Please enter your full name ")
        elif len(full_name) <3:
            errors.append("name must be at least 3 character")

        
        # validate phone number
        if not phone_number:
            errors.append("please enter your mobile number")
        elif not phone_number.replace("+","").replace("-","").replace(" ","").isdigit():
            errors.append("phone number must be contain 10 digit")
        elif len(phone_number.replace("+","").replace("-","").replace(" ","")) < 10:
            errors.append("phone number must be at least 10 digit ")

        # if there an error , return to form with the error
        if errors:
            return render(request,"core/appoinment.html",{
                "errors":errors,
                "department":department,
                "doctor": doctor,
                "appointment_date":appointment_date,
                "appointment_time":appointment_time,
                "full_name":full_name,
                "phone_number":phone_number,
                "message":message})
        existing_appointment =Appointment.objects.filter(
            phone_number = phone_number,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()
        
        if existing_appointment:
            return render(request,"core/appoinment.html",{
                "errors":['you already have an appointment scheduled at this date and time'],
                "department":department,
                "doctor": doctor,
                "appointment_date":appointment_date,
                "appointment_time":appointment_time,
                "full_name":full_name,
                "phone_number":phone_number,
                "message":message

            })
        
        # Create appointment
        try:
            Appointment.objects.create(
                department=department,
                doctor= doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                full_name=full_name,
                phone_number=phone_number,
                message=message

            )
            return render(request,"core/appoinment_successfull.html",{
                'name':full_name
            })
        except Exception as e:
            return render(request,"core/appoinment.html",{
                "errors":[f"Error creating appoinment:{str(e)}"],
                "department":department,
                "doctor": doctor,
                "appointment_date":appointment_date,
                "appointment_time":appointment_time,
                "full_name":full_name,
                "phone_number":phone_number,
                "message":message


            })
    return render(request,"core/appoinment.html")        
           


def view_subscribefooter(request):
    if request.method =="POST":
        subscribe= subscribefooter.objects.create(
            email=request.POST.get("email","")
        )
        return render(request,"core/emailsuccessfull.html",{"emailname":subscribe.email})

# single blog page
def view_singleblog(request):
    email=request.POST.get("email","")
    # check if the email is already exist
    if singleblogModel.objects.filter(email=email).exists():
        return render(request,"core/single_blog.html",{
            'error':'you have already commented with this email'
        })
    if request.method =="POST":
        blog =singleblogModel.objects.create(
            name=request.POST.get("name",""),
            email=email,
            message=request.POST.get("message","")
        )
        return render(request,"core/singleblogsuccessfull.html",{"blogname":blog.name})
    return render(request,"core/single_blog.html")