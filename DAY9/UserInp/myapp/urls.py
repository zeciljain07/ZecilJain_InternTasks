from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview, name="Home"),
    path('about',views.aboutpageview, name="About Us"),
    path('contact',views.contactpageview, name="Contact Us"),
    path('form',views.myform, name="My Form"),
    path('formprocess',views.process, name="Process"),  
    
]