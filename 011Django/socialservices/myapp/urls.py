

from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
   
   path('sms',sendmsg,name="sms"),
   path('email',sendemail,name="email")
]
