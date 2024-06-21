
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('reg/',reg,name="reg"),
    path('home/',home,name="home"),
    path('logout/',logout_view,name="logout")
]
