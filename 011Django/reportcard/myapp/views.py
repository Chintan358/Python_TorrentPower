from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
def index(request):

   

    studentdata = Studnet.objects.all();

    paginator = Paginator(studentdata, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html',{'studentdata':page_obj})

def viewMarks(request,id):
    marks = Marks.objects.filter(student_id__student_id__student_id=id);

    # print all marks in the list.
    sum = 0;
    for i in marks:
        sum = sum + i.marks


    data =   Studnet.objects.annotate(total = Sum("marks__marks")).order_by('-total')
    rank = 1;
    for i in data:
        if i.student_id.student_id == id:
            break;
        rank=rank+1
    

    return render(request, 'viewMarks.html',{'marks':marks,'id':marks[0].student_id.student_id.student_id,'name':marks[0].student_id.name,'email':marks[0].student_id.email,"total":sum,"rank":rank});
    
def sendMail(request,id):
    marks = Marks.objects.filter(student_id__student_id__student_id=id);

    # print all marks in the list.
    sum = 0;
    for i in marks:
        sum = sum + i.marks


    data =   Studnet.objects.annotate(total = Sum("marks__marks")).order_by('-total')
    rank = 1;
    for i in data:
        if i.student_id.student_id == id:
            break;
        rank=rank+1
    
    subject = 'Report Card'
    html_message = render_to_string('viewMarks.html',{'marks':marks,'id':marks[0].student_id.student_id.student_id,'name':marks[0].student_id.name,'email':marks[0].student_id.email,"total":sum,"rank":rank})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [marks[0].student_id.email]
    send_mail( subject, plain_message, email_from, recipient_list ,html_message=html_message)
    
    return HttpResponse("email sent successfully")


    
    