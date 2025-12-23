from django.urls import path
from .views import *


urlpatterns= [
    path("home/",view_home, name='home'),
    path("about/",view_about, name='about'),
    path("service/",view_service, name='service'),
    path("department/",view_department, name='department'),
    path("single_department",view_single_department, name='single_department'),
    path("doctor/",view_doctor,name="doctor"),
    path("single_doctor/",view_singledoctor,name="single_doctor"),
    path("blog/",view_blog_sidebar,name="blog"),
    path("single_blog/",view_single_blog,name="single_blog"),
    path("contact/",view_contact,name="contact"),
    path("appoinment/",view_appoinment,name="appoinment"),

]