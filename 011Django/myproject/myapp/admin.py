from django.contrib import admin
from .models import *
# Register your models here.

class UserDisplay(admin.ModelAdmin):
    list_display = ['username','email','phone','age']


admin.site.register(User,UserDisplay)
