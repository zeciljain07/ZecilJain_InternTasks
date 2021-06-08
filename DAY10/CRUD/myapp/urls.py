from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview, name="Home"),
    path('about',views.aboutpageview, name="About Us"),
    path('contact',views.contactpageview, name="Contact Us"),
    path('dlist',views.driverlist.as_view(), name="Driver"),
    path('clist',views.constructorlist.as_view(), name="Constructors"),
]