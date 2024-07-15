

from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
   
   path('sms',sendmsg,name="sms"),
   path('email',sendemail,name="email"),
   path('email_attach',sendmail_with_attachment,name='email_attach'),
   path('email_temp',sendmail_with_template,name="email_temp")
]
