from django.shortcuts import render,HttpResponse
import requests
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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


def sendmail_with_attachment(request):

    subject = 'Test'
    message = "Testing..mail"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chintan.tops@gmail.com']
    user = EmailMessage(subject=subject,body=message,from_email=email_from,to=recipient_list)
    filepath = f"{settings.BASE_DIR}/data.pdf"# replace with the actual path to your file
    user.attach_file(filepath)
    user.send()   
    return HttpResponse("email sent successfully")

def sendmail_with_template(request):
    
    subject = 'welcome to GFG world'
    html_message = render_to_string('index.html',{'username':"Rahul"})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["chintan.tops@gmail.com"]
    send_mail( subject, plain_message, email_from, recipient_list ,html_message=html_message)
    return HttpResponse("email sent successfully")