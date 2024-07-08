from django.shortcuts import render,HttpResponse
import requests
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
# Create your views here.
def sendmsg(request):

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"API-KEY","message":"This is test message","language":"english","route":"q","numbers":"9586926902"}

    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return HttpResponse("message sent successfully")
    
def sendemail(request):
     

    subject = 'Test'
    message = "Testing..mail"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("email sent successfully")