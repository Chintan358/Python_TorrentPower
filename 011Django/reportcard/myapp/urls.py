
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("viewmarks/<id>",viewMarks,name="viewmarks"),
     path("sendmail/<id>",sendMail,name="sendmail")
]
