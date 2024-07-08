from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
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
    