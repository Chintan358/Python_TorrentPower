
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path("", index,name="index"),
    path("addstudent",addstudent,name="addstudent"),
    path("loadstudents",loadstudents,name="loadstudents"),
    path("deleteStudent",deleteStudent,name="deleteStudent"),
    path("getStudent",getStudent,name="getStudent"),
    path("editStudent",editStudent,name="editStudent"),
    path("searchstudent",searchstudent,name="searchstudent")
]